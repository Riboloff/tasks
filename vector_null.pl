#! /usr/bin/perl

use strict;
use warnings;

use utf8;
use v5.10;

use Data::Dumper;
use open ':std', ':encoding(utf8)';
use Test::More;


my @tests = (
    ['0123456789', '1234567890'],
    ['123400567890', '123456789000'],
    ['1023400567800090', '1234567890000000'],
    ['1023400000567800090', '1234567890000000000'],
    ['00123045678900', '12345678900000'],
    ['01020300405060708090', '12345678900000000000'],
);

for (@tests) {
    is(move_zero($_->[0]), $_->[1], 'string ' . $_->[0]);
}


sub move_zero {
    my $str = shift;

    my @array = split(//, $str);

    my $p_r = 0;
    my $p_l = 0;
    while ($p_r < @array) {
        my $v_l = $array[$p_l];
        my $v_r = $array[$p_r];

        if ($array[$p_r] eq 0) {
            $p_r++;
            next;
        }
        if ($array[$p_l] eq 0) {
            while ($array[$p_r] eq 0) {
                $p_r++;
            }
        }

        if ($p_r > $p_l) {
            $array[$p_l] = $array[$p_r];
        }

        $p_l++;
        $p_r++;
    }

    for (my $i = $p_l; $i < @array; $i++) {
        $array[$i] = 0;
    }

    my $out = join('', @array);

    say $out;
    return $out;
}
