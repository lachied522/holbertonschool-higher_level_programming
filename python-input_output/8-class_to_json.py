#!/usr/bin/python3
"""
This is a module docstring
"""
import json


def class_to_json(obj):
    return json.dumps(obj.__dict__)
