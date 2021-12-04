#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.34);
use experimental qw(signatures);
use List::Util qw(sum);

my $gt = sub ($x, $y) {return $x > $y};
my $lt = sub ($x, $y) {return $x < $y};

sub calc_rating($report, $op, $tie) {
    my %valid = map {$_ => 1} 0..$#$report;
    my $col = 0;
    while (keys(%valid) > 1) {
        my @keys = keys %valid;

        # are we looking for 0s or 1s?
        my $half = @keys / 2;
        my $cnt = sum map{$report->[$_][$col]} @keys;
        my $common;
        if ($op->($cnt, $half)) {
            $common = 1;
        } elsif ($cnt == $half) {
            $common = $tie;
        } else {
            $common = 0;
        }

        # now remove the rows where the keys don't match from valid
        for my $k (@keys) {
            delete $valid{$k} unless $report->[$k][$col] == $common;
        }
        $col++;
    }
    # convert remaining row to binary
    my @keys = keys %valid;
    if (@keys != 1) {
        die "still have " . scalar @keys . "rows left";
    }
    my $s = '0b' . join "", $report->[$keys[0]]->@*;
    return eval $s;
}

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

my $oxygen_rating = calc_rating(\@report, $gt, 1);
my $co2_rating = calc_rating(\@report, $lt, 0);
say "Part 2: ", $oxygen_rating * $co2_rating;
