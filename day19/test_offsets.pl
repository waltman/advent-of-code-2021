#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.32);
use experimental qw(signatures);
use autodie;

my $fh;
my @off1;
open $fh, '<', "off1.txt";
while (<$fh>) {
    chomp;
    push @off1, [split ','];
}
my @off2;
open $fh, '<', "off2.txt";
while (<$fh>) {
    chomp;
    push @off2, [split ','];
}

for my $i (0..11) {
    my $ar1 = $off1[$i];
    my $ar2 = $off2[$i];
    printf "%d, %d, %d\n", $ar2->[0] + $ar1->[0], -$ar2->[1] + $ar1->[1], $ar2->[2] + $ar1->[2];
}

