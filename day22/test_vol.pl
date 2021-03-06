#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.34);
use experimental qw(signatures);

# let's see what the total volume is here...
my $tot = 0;
my ($minx, $maxx, $miny, $maxy, $minz, $maxz) = (1e300, -1e300, 1e300, -1e300, 1e300, -1e300);
while (<>) {
    chomp;
    m/x=([\-\d]+)\.\.([\-\d]+),y=([\-\d]+)\.\.([\-\d]+),z=([\-\d]+)\.\.([\-\d]+)/;
#    say $_;
#    say "$1 $2 $3 $4 $5 $6";
    my $vol = ($2 - $1 + 1) * ($4 - $3 + 1) * ($6 - $5 + 1);
#    say $vol;
    $tot += $vol;
    $minx = $1 if $1 < $minx;
    $miny = $3 if $3 < $miny;
    $minz = $5 if $5 < $minz;
    $maxx = $2 if $2 > $maxx;
    $maxy = $4 if $4 > $maxy;
    $maxz = $6 if $6 > $maxz;
}

say $tot;
say "x: $minx $maxx ", $maxx-$minx+1;
say "y: $miny $maxy ", $maxy-$miny+1;
say "z: $minz $maxz ", $maxz-$minz+1;
