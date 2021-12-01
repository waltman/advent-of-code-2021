#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.34);
use experimental qw(signatures);
use List::Util qw(sum);

my @depth;
while (<>) {
    chomp;
    push @depth, $_;
}

say "Part 1: ", count_larger(\@depth);

my @windows = map { sum(@depth[$_..$_+2]) } 0..$#depth-2;
say "Part 2: ", count_larger(\@windows);

sub count_larger($a) {
    my $cnt = 0;
    for my $i (1..$#$a) {
        $cnt++ if $a->[$i] > $a->[$i-1];
    }
    return $cnt;
}
