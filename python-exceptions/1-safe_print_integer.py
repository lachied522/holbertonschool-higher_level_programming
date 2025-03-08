#!/usr/bin/python3

def safe_print_integer(value):
    num_printed = 0

    try:
        print("{:d}".format(value))

        return True
    except Exception:
        return False
