#!/usr/bin/perl
# kate: space-indent off;

# Copyright 2016-2021 Luke Dashjr
# Note this is presently NOT free software. See LICENSE for details.
# Use at your own risk. No warranty.

use strict;
use warnings;

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
	while ($_ = shift @to_process) {
		print "$_\n";
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

