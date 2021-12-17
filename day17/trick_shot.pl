#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.34);
use experimental qw(signatures);
use List::Util qw(max);

sub hit_target($x1, $x2, $y1, $y2, $vix, $viy) {
    my ($x, $vx, $y, $vy) = (0, $vix, 0, $viy);
    while (1) {
	$x += $vx;
	$vx = max(0, $vx-1);
	$y += $vy--;
	if ($x1 <= $x <= $x2 && $y1 <= $y <= $y2) {
	    return 1;
	} elsif ($x > $x2 || $y < $y1) {
	    return 0;
	}
    }
}

# parse input
my $line = <>;
chomp $line;
$line =~ /x=([\d\-]+)\.\.([\d\-]+), y=([\d\-]+)\.\.([\d\-]+)/;
my ($x1, $x2, $y1, $y2) = ($1, $2, $3, $4);

# part 1
my $best_ymax = "-inf";
for my $vi (0..1000) {
    my ($v, $y, $ymax) = ($vi, 0, 0);
    while (1) {
	$y += $v;
	$ymax = max($ymax, $y);
	if ($y1 <= $y <= $y2) {
	    $best_ymax = max($best_ymax, $ymax);
	    last;
	} elsif ($y < $y1) {
	    last;
	} else {
	    $v--;
	}
    }
}
say "Part 1: ", $best_ymax;

# part 2
my $cnt = 0;
for my $vix (0..$x2) {
    for my $viy ($y1..500) {
	$cnt++ if hit_target($x1, $x2, $y1, $y2, $vix, $viy);
    }
}
say "Part 2: ", $cnt;
