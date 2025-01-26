#!/usr/bin/python3
"""
This is a dosctring to describe what this module does.
"""
def add_integer(a, b=98):
    """
    Adds two numbers, float or integer.
    a: int or float
    b: int or float
    """
    if not (isinstance(a, float) or isinstance(a, int)):
        raise TypeError("a must be an integer")

    if not (isinstance(b, float) or isinstance(b, int)):
        raise TypeError("a must be an integer")

    return (int(a) + int(b))
