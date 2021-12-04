#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.34);
use experimental qw(signatures);
use List::Util qw(sum);

my @report;
while (<>) {
    chomp;
    push @report, [split //];
}

my $gamma = '0b';
my $eps = '0b';
my $half = @report / 2;
for my $col (0..$#{$report[0]}) {
    my $sum = sum map {$report[$_][$col]} (0..$#report);
    if ($sum > $half) {
        $gamma .= 1;
        $eps .= 0;
    } else {
        $gamma .= 0;
        $eps .= 1;
    }
}

say "Part 1: ", eval($gamma) * eval($eps);
