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
