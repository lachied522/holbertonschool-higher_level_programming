#!/usr/bin/python3
"""
This is a module docstring
"""


class Rectangle:
    """
    This is a class docstring
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialiases an instance of this class
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Prints rectange as string
        """
        if self.height == 0 or self.width == 0:
            return ""

        rect_string = ""
        for i in range(self.height):
            for j in range(self.width):
                rect_string += str(self.print_symbol)
            if i < self.height - 1:
                rect_string += "\n"

        return rect_string

    def __repr__(self):
        """
        Returns string representation of instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return bigger rectangle by area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

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

    def area(self):
        """
        Calculate instance area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate instance perimiter
        """
        if self.width > 0 and self.height > 0:
            return 2 * (self.width + self.height)
        return 0
