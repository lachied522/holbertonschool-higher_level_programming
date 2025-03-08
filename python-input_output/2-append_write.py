#!/usr/bin/python3
"""
This is a module docstring
"""


def append_write(filename="", text=""):
    """
    This is a function docstring
    """

    n = 0

    with open(filename, "a", encoding="utf-8") as f:
        n = f.write(text)

    return n
