#!/usr/bin/python3
"""
This a module docstring
"""


class Square:
    """
    This is a class dosctring
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise a Square instance with size and position

        Args:
            size (int): size of square, must be positive integer
            position (tuple): coordinates of square in x y plane
                              must be positive
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size property
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
