#!/usr/bin/python3

def is_same_class(obj, a_class):
    return type(obj).__name__ == a_class.__name__
