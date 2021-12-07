#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.34);
use experimental qw(signatures);
use List::Util qw(sum min max);

sub cost($x, $y) {
    my $dist = abs($x-$y);
    return $dist * ($dist + 1) / 2;
}

my @crabs = split ',', <>;
chomp $crabs[-1];

my ($best_pos, $best_fuel) = (0, 1e300);

for my $pos (min(@crabs) .. max(@crabs)) {
    my $fuel = sum map { abs $crabs[$_] - $pos } 0..$#crabs;
    ($best_pos, $best_fuel) = ($pos, $fuel) if $fuel < $best_fuel;
}
say "Part 1: ", $best_fuel, ' ', $best_pos;

($best_pos, $best_fuel) = (0, 1e300);
for my $pos (min(@crabs) .. max(@crabs)) {
    my $fuel = sum map { cost($crabs[$_],$pos) } 0..$#crabs;
    ($best_pos, $best_fuel) = ($pos, $fuel) if $fuel < $best_fuel;
}
say "Part 2: ", $best_fuel, ' ', $best_pos;

say "mean: ", sum(@crabs) / @crabs;
my @sorted = sort {$a <=> $b} @crabs;
say "median: $sorted[@sorted/2]";
