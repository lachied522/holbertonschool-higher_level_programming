#!/usr/bin/python3

def value_at_index(my_tuple, i):
    if i > len(my_tuple) - 1:
        return 0
    return my_tuple[i]


def add_tuple(tuple_a=(), tuple_b=()):
    sum_a = value_at_index(tuple_a, 0) + value_at_index(tuple_b, 0)
    sum_b = value_at_index(tuple_a, 1) + value_at_index(tuple_b, 1)
    return sum_a, sum_b
