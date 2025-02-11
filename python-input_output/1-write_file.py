#!/usr/bin/python3
"""
This is a module docstring
"""


def write_file(filename="", text=""):
    """
    This is a function docstring
    """

    n = 0

    with open(filename, "w", encoding="utf-8") as f:
        n = f.write(text)

    return n
