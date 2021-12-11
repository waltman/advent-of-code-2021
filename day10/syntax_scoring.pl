#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.34);
use experimental qw(signatures);

my %POINTS = ( ')' => 3,
	       ']' => 57,
	       '}' => 1197,
	       '>' => 25137,
	     );

my %MATCH = ( '(' => ')',
	      ')' => '(',
	      '[' => ']',
	      ']' => '[',
	      '{' => '}',
	      '}' => '{',
	      '<' => '>',
	      '>' => '<',
	    );

my %AUTOCOMPLETE_POINTS = ( ')' => 1,
			    ']' => 2,
			    '}' => 3,
			    '>' => 4,
			  );

my $error_score;
my @autocomplete_scores;
while (<>) {
    chomp;
    my @stack;
    for my $c (split //) {
	if (defined $AUTOCOMPLETE_POINTS{$c}) {
	    if (@stack == 0 || $stack[-1] ne $MATCH{$c}) {
		$error_score += $POINTS{$c};
		@stack = ();
		last;
	    } else {
		pop @stack;
	    }
	} else {
	    push @stack, $c;
	}
    }
    if (@stack) {
	my $score = 0;
	while (my $c = pop @stack) {
	    $score = 5 * $score + $AUTOCOMPLETE_POINTS{$MATCH{$c}};
	}
	push @autocomplete_scores, $score;
    }
}

say "Part 1: ", $error_score;
my @tmp = sort {$a <=> $b} @autocomplete_scores;
say "Part 2: $tmp[int(@tmp/2)]";
