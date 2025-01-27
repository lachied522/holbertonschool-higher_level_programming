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
        self.position = position

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

    @property
    def position(self):
        """
        Getter for position property
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position property
        """
        if not (
            isinstance(value, tuple)
            and len(value) == 2
            and isinstance(value[0], int)
            and isinstance(value[1], int)
            and value[0] >= 0
            and value[1] >= 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Return area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print square in plane
        """
        size = self.size
        x_start = self.position[0]
        y_start = self.position[1]

        if size == 0:
            print("")
            return

        for y in range(y_start):
            print("")

        for i in range(size):
            for x in range(x_start):
                print(" ", end="")

            for j in range(size):
                print("#", end="")
            print("")
