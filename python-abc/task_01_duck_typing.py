"""
This is a module docstring
"""
#!/usr/bin/env python3

from abc import ABC, abstractmethod

import math

class Shape(ABC):
    """
    This is a class docstring
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    This is a class docstring
    """

    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    This is class docstring
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
