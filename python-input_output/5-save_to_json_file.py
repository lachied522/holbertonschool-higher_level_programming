#!/usr/bin/python3
"""
This is a module docstring
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This is a function docstring
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
