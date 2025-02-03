#!/usr/bin/python3
"""
This is a module docstring
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    Class that inherits from BaseGeometry
    """

    def __init__(self, size):
        self.__size = self.integer_validator("size", size)
