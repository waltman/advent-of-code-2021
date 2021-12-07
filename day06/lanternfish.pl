#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.34);
use List::Util qw(sum);

my @fish = (0) x 9;
$fish[$_]++ for split ',', <>;

for my $day (1..256) {
    @fish = (@fish[1..$#fish], $fish[0]);
    $fish[6] += $fish[8];

    if ($day == 80) {
        say "Part 1: ", sum(@fish);
    } elsif ($day == 256) {
        say "Part 2: ", sum(@fish);
    }
}
