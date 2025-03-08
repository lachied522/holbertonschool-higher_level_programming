#!/usr/bin/python3
"""
This is a module docstring
"""


def is_same_class(obj, a_class):
    """
    Check if object is exactly an instance of a class
    """
    return type(obj).__name__ == a_class.__name__
