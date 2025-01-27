#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):    
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (
                isinstance(value, tuple)
                and isinstance(value[0], int)
                and isinstance(value[1], int)
            ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
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

