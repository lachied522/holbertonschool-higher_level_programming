"""
This is a module docstring
"""
#!/usr/bin/env python3

class CountedIterator:
    """
    This is a class docstring
    """

    def __init__(self, items):
        self.__iter = iter(items)
        self.__count = 0

    def __next__(self):
        value = next(self.__iter)
        self.__count += 1
        return value

    def get_count(self):
        return self.__count
