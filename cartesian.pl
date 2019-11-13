#!/usr/bin/perl

use strict;;
use warnings;

use Data::Dumper;

my %input = (
    2 => ['DM1', 'DM2'],
    1 => ['Foo', 'bar', 'baz'],
    3 => 'source',
    4 => ['csv'],
);

print Dumper(cartesian(\%input));

sub cartesian {
    my ($input) = @_;

    my @output = ();

    my @position = sort {$a <=> $b} keys %$input;

    for my $item (@{$input->{$position[0]}}) {
        push(@output, [$item]);
    }

    for my $i (1 .. $#position) {
        my $pos = $position[$i];
        my $items = $input->{$pos};
        if (ref $items ne 'ARRAY') {
            $items = [$items];
        }

        my @output_copy = @output;
        @output = ();
        for my $item (@$items) {
            for my $str (@output_copy) {
                push(@output, [@$str, $item]);
            }
        }
    }

    return \@output;
}
