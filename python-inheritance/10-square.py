#!/usr/bin/python3
"""
This is a module docstring
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that inherits from BaseGeometry
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
