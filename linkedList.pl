package Node;

sub new {
    my ($class, $value) = @_;

    return bless {value => $value, next => undef}, $class;
}

package LinkedList;

sub new {
    my ($class, $head) = @_;

    my $node = Node->new($head);
    
    return bless {head => $node}, $class;
}

sub add {
    my ($self, $value) = @_;

  
    my $node = $self->{head};
    while (defined $node->{next}) {
        $node = $node->{next};
    }
    $node->{next} = Node->new($value);
}

sub out {
    my ($self) = @_;

    my $node = $self->{head};
    while ($node) {
        print $node->{value}, "\n";
        $node = $node->{next};
    }
}

sub revers {
    my ($self) = @_;

    my $current = $self->{head};
    my $next = undef;
    my $prev = undef;

    while (defined $current) {
        $next = $current->{next};
        $current->{next} = $prev;
        $prev = $current;
        $current = $next;
    }

    $self->{head} = $prev;
    return $prev;
}

package main;
use Data::Dumper;
use strict;
use warnings;

my $ll = LinkedList->new(1); 
$ll->add(2);
$ll->add(3);
$ll->add(4);
$ll->out();
$ll->revers();
print Dumper($ll);


