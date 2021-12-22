#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.34);
use experimental qw(signatures);

# let's see what the total volume is here...
my $tot = 0;
while (<>) {
    chomp;
    m/x=([\-\d]+)\.\.([\-\d]+),y=([\-\d]+)\.\.([\-\d]+),z=([\-\d]+)\.\.([\-\d]+)/;
    say $_;
    say "$1 $2 $3 $4 $5 $6";
    my $vol = ($2 - $1 + 1) * ($4 - $3 + 1) * ($6 - $5 + 1);
    say $vol;
    $tot += $vol;
}

say $tot;
