#!/usr/bin/python3
"""
This is a module docstring
"""


class MyList(list):
    """
    Custom list class that inherits from built in list
    """

    def print_sorted(self):
        """
        Print sorted items
        """
        print(sorted(self))
