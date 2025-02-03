#!/usr/bin/python3
"""
This is a module docstring
"""


class BaseGeometry:
    """
    Custom list class that inherits from built in list
    """

    def __init__(self):
        pass

    def integer_validator(self, name, value):
        """
        Helper function for checking if value is an integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if not value > 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        raise Exception("area() is not implemented")
