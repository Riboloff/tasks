#! /usr/bin/perl

use strict;
use warnings;

use utf8;

use Data::Dumper;
#use JSON;
use JSON::XS;
use Tie::File;

use feature 'say';


my $today = {
    holiday => 1,
    before_holiday => 1,
    wday => 1, #понедельник
};

my $time_table = {
    '1,2,5' => 'middle',
    '5,weekend' => 'top',
    'weekend,holiday' => 'bottom',
};


my $table = parse_table($time_table);
say get_position($table, $today);

sub parse_table {
    my ($time_table) = @_;

    my %time_table_days = ();
    for my $key (keys %$time_table) {
        for my $day (split(/,/, $key)) {
            if ($day eq '7') {
                $day = 0;
            }
            $time_table_days{$day} = $time_table->{$key};
        }
    }

    return \%time_table_days;   
}

sub get_position {
    my ($table, $today) = @_;

    if ($today->{holiday} and $table->{holiday}) {
        return $table->{holiday};
    }

    if ($today->{before_holiday} and $table->{before_holiday}) {
        return $table->{before_holiday}
    }

    if ($today->{wday} ~~ [0,6] and $table->{weekend}) {
        return $table->{weekend};
    }

    if ($today->{wday} ~~ [1 .. 5] and $table->{workday}) {
        return $table->{workday};
    }

    return $table->{$today->{wday}};
}
