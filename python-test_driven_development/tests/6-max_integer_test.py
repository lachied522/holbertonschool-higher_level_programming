#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):

    def ordered_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def unordered_max(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def negative_numbers(self):
        self.assertEqual(max_integer([-1, -2]), -1)

    def empty(self):
        self.assertEqual(max_integer([]), None)

    def string_type(self):
        self.assertRaises(TypeError, max_integer(["hello"]))


if __name__ == "__main__":
    unittest.main()
