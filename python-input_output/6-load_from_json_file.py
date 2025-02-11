#!/usr/bin/python3
"""
This is module docstring
"""
import json


def load_from_json_file(filename):
    """
    This is a function docstring
    """
    with open(filename, "r") as f:
        return json.load(f)
