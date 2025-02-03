#!/usr/bin/python3
"""
This is a module docstring
"""


def inherits_from(obj, a_class):
    """
    Check if object is inherited from a class
    """
    return isinstance(obj, a_class) and type(obj).__name__ != a_class.__name__
