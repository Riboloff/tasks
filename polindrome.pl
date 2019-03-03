#! /usr/bin/perl

use strict;
use warnings;

use utf8;
use v5.10;

use Data::Dumper;
use open ':std', ':encoding(utf8)';
use Test::More;

my @tests = (
    ['Казак', 1],
    ['А роза упала на лапу Азора', 1],
    ['Do geese see God?', 1],
    ['Madam, Im Adam', 1],
    ['Каза', 0],
    ['Каза кк', 0],
);

for (@tests) {
    is(is_polindrome($_->[0]), $_->[1], $_->[0]);
}


sub is_polindrome {
    my $str = shift;

    my @string = split(//, $str);
    my $start = 0;
    my $end = $#string;

    while ($start < $end) {
        my $l_symbol = $string[$start];
        my $r_symbol = $string[$end];
        if ($l_symbol !~ /^\w$/) {
            $start++;
            next;
        }
        if ($r_symbol !~ /^\w$/) {
            $end--;
            next;
        }
        if (lc $l_symbol eq lc $r_symbol) {
            $start++;
            $end--;
        }
        else {
            return 0;
        }
    }

    return 1;
}
