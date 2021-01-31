#!/usr/bin/perl
# kate: space-indent off;

# Copyright 2016-2021 Luke Dashjr
# Note this is presently NOT free software. See LICENSE for details.
# Use at your own risk. No warranty.

use strict;
use warnings;
use forks;
use utf8;

BEGIN { binmode STDOUT, ":utf8" }

use File::Basename;
use HTTP::Request;
use JSON::PP;
use LWP;

my $cachedir = dirname(__FILE__) . "/getinfo-to-html-cache/";

warn "Remember to wipe cache if PRs might have been merged!\n";

my @github_auth;
{
	open my $f, "<&3" or die;
	@github_auth = <$f>;
	close $f;
}

my @to_process;

my %sortorder = (
	"\@" => 0,
	"PR" => 1,
	"BM" => 2,
	"LA" => 2,
);

sub prep_html {
	@to_process = sort {
		my ($aa, $bb) = ($a, $b);
		$aa =~ s/^(\S+) // or die;
		my $ka = $1;
		$bb =~ s/^(\S+) // or die;
		my $kb = $1;
		my $sod = $sortorder{$ka} <=> $sortorder{$kb};
		return $sod if $sod;
		if ($ka eq 'PR') {
			$aa += 1000000 if $aa =~ s/^g//;
			$bb += 1000000 if $bb =~ s/^g//;
			return $aa <=> $bb
		}
		$aa cmp $bb
	} @to_process;
	my @threads;
	my $i;
	while ($_ = shift @to_process) {
		my $line = $_;
		push @threads, async {
			if (s/^PR ((g)?(.*))//) {
				my ($prspec, $is_gui, $prnum) = @{^CAPTURE};
				my $j;
				if (-e "$cachedir/$prspec") {
					open my $f, "<$cachedir/$prspec";
					my $content;
					{
						local $/ = undef;
						$content = <$f>;
					}
					close $f;
					$j = decode_json $content;
				} else {
					my $repo;
					if (defined $is_gui) {
						$repo = "bitcoin-core/gui";
					} else {
						$repo = "bitcoin/bitcoin";
					}
					my $req = HTTP::Request->new(GET => "https://api.github.com/repos/$repo/pulls/$prnum");
					$req->authorization_basic(@github_auth);
					my $content = LWP::UserAgent->new->request($req)->content;
					$j = decode_json $content;
					die $content unless $j->{title};
					
					open my $f, ">$cachedir/$prspec";
					print $f $content;
					close $f;
				}
				$_ = "<a";
				$_ .= " class=\"merged\"" if $j->{merged};
				$_ .= " href=\"" . $j->{"html_url"} . "\">" . $j->{title} . "</a>";
			}
			"$_\n"
		};
		if ($line =~ /^PR /) {
			if (not $i++) {  # First PR job runs synchronously to init LWP
				while (@threads) {
					my $thread = shift @threads;
					print $thread->join;
				}
			}
		}
		while (@threads > 4) {
			my $thread = shift @threads;
			print $thread->join;
		}
	}
	for my $thread (@threads) {
		print $thread->join;
	}
}

while (my $line = <>) {
	chomp $line;
	if ($line =~ m[^\@]) {
		prep_html;
	}
	push @to_process, $line;
}
prep_html;

