#!/usr/bin/python3
def uppercase(string):
    upper_string = ""
    for c in string:
        if ord('a') <= ord(c) and ord(c) <= ord('z'):
            upper_string += chr(ord(c) - ord('a') + ord('A'))
        else:
            upper_string += c

    print(upper_string)
