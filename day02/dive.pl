#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.34);
use experimental qw(signatures);

my @cmds;
while (<>) {
    chomp;
    my ($cmd, $val) = split / /;
    push @cmds, [$cmd, $val];
}

my ($d, $h, $a) = (0,0,0);
for (@cmds) {
    my ($cmd, $val) = $_->@*;
    if ($cmd eq 'forward') {
        $h += $val;
    } elsif ($cmd eq 'down') {
        $d += $val;
    } elsif ($cmd eq 'up') {
        $d -= $val;
    }
}
say "Part 1: ", $d * $h;

($d, $h, $a) = (0,0,0);
for (@cmds) {
    my ($cmd, $val) = $_->@*;
    if ($cmd eq 'forward') {
        $h += $val;
        $d += $a * $val;
    } elsif ($cmd eq 'down') {
        $a += $val;
    } elsif ($cmd eq 'up') {
        $a -= $val;
    }
}
say "Part 2: ", $d * $h;
