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
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
