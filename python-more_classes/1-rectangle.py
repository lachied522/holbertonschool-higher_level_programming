#!/usr/bin/python3
"""
This is a module docstring
"""


class Rectangle:
    """
    This is a class docstring
    """
    def __init__(self, width=0, height=0):
        """
        Initialiases an instance of this class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter for width attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
