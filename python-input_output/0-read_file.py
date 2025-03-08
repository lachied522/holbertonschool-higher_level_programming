#!/usr/bin/python3
"""
This is a module docstring
"""


def read_file(filename=""):
    """
    This is a function docstring
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            print(line, end='')
