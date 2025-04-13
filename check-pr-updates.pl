#!/usr/bin/perl
# kate: space-indent off;

# Copyright 2016-2021 Luke Dashjr
# Note this is presently NOT free software. See LICENSE for details.
# Use at your own risk. No warranty.

use sort 'stable';
use strict;
use warnings;
use forks;
use utf8;

my $min_firstseen = shift || 0;

BEGIN { binmode STDOUT, ":utf8" }

use File::Basename;
use HTML::Entities;
use HTTP::Request;
use JSON::PP;
use List::Util qw(max);
use LWP;
use Time::Piece;

my $cachedir = dirname(__FILE__) . "/geninfo-to-html-cache/";

warn "Remember to wipe cache!\n";

my @github_auth;
{
	open my $f, "<&3" or die;
	@github_auth = <$f>;
	close $f;
	chomp for @github_auth;
}

sub makegitcmd {
	("git", "--no-pager", @_)
}

sub syscapture {
	my @cmd = @_;
	#print "@cmd\n";
	open(my $outio, "-|", @cmd);
	my $out;
	{
		local $/;
		$out = <$outio>;
	}
	close $outio;
	my $ec = $?;
	($ec, $out)
}

sub gitcapture {
	my @cmd = makegitcmd(@_);
	my ($ec, $out) = syscapture(@cmd);
	chomp $out;
	die "@cmd failed (exit code $ec; output $out)" if $ec;
	$out
}

sub wc_l {
	return 0 unless length $_[0];
	1 + ($_[0] =~ tr/\n//)
}

sub github_fetch_prinfo {
	my ($prspec) = @_;
	$prspec =~ m[([gk]?)(.*)] or die;
	my ($is_gui, $prnum) = @{^CAPTURE};
	
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
		if ("g" eq $is_gui) {
			$repo = "bitcoin-core/gui";
		} elsif ("k" eq $is_gui) {
			$repo = "bitcoinknots/bitcoin";
		} else {
			$repo = "bitcoin/bitcoin";
		}
		warn "Fetching $prspec info...";
		my $req = HTTP::Request->new(GET => "https://api.github.com/repos/$repo/pulls/$prnum");
		$req->authorization_basic(@github_auth);
		my $content = LWP::UserAgent->new->request($req)->content;
		$j = decode_json $content;
		die $content unless $j->{title} or ($j->{status} ||0) eq 404;

		open my $f, ">$cachedir/$prspec";
		print $f $content;
		close $f;
	}
	$j
}

my $re_potential_pr = qr[\b(?:[kg]\d+|(?:gui|knots)\#\d+|\d{5})\b];

open my $gitlog, "git log --reverse -p --format='TS:%at' |";

my $then;
my $fn;
my $skip = 1;
my %firstseen;
while (my $line = <$gitlog>) {
	chomp $line;
	if ($line =~ m[^TS:(\d+)$]) {
		$then = $1;
	} elsif ($line =~ m[^\+{3} b/(.*)$]) {
		$fn = $1;
		$skip = $fn !~ m[\.spec$];
	} elsif ($skip) {
	} else {
		die if pos($line);
		$line =~ m[.*?#]g or next;
		while($line =~ m[\G.*?($re_potential_pr)]g) {
			my $pr = $1;
			$pr =~ s[(gui|knots)\#][substr $1, 0, 1]e;
			next if exists $firstseen{$pr};
			$firstseen{$pr} = max($then, $min_firstseen);
		}
	}
}

my %lastactivity;
while (my $line = <>) {
	chomp $line;
	$line =~ m[.*?#]g or next;
	while ($line =~ m[\G.*?($re_potential_pr)]g) {
		my $pr = $1;
		$pr =~ s[(gui|knots)\#][substr $1, 0, 1]e;
		die unless exists $firstseen{$pr};
		next if exists $lastactivity{$pr};
		
		my $j = github_fetch_prinfo($pr);
		if (($j->{status} || 0) eq 404) {
			$lastactivity{$pr} = undef;
			print "$pr\t$firstseen{$pr}\tNOT FOUND\n";
			next
		}
		$lastactivity{$pr} = Time::Piece->strptime($j->{updated_at}, "%Y-%m-%dT%H:%M:%SZ")->epoch;
		
		next if $firstseen{$pr} > $lastactivity{$pr};
		
		print "$pr\t$firstseen{$pr}\t$lastactivity{$pr} ".$j->{head}->{label}."\n";
	}
}
