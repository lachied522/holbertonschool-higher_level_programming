#!/usr/bin/python3
"""
This is a module docstring
"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

DEFAULT_FILENAME = "add_item.json"

def append_to_file(items_to_add, filename=DEFAULT_FILENAME):
    try:
        all_items = load_from_json_file(filename)
    except FileNotFoundError:
        all_items = []

    for item in items_to_add:
        all_items.append(item)

    save_to_json_file(all_items, filename)

if __name__ == "__main__":
    append_to_file(sys.argv[1:])
