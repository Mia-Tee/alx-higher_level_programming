#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """a function that adds two tuples"""
    tuple_a = tuple_a + (0, 0)
    """addition of the first element of each arguement"""
    tuple_b = tuple_b + (0, 0)
    """addition of the second element of each arguement"""
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
