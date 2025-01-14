#!/usr/bin/python3
def uppercase(string):
    for c in string:
        if ord('a') <= ord(c) and ord(c) <= ord('z'):
            print("{:c}".format(ord(c) - ord('a') + ord('A')), end='')
        else:
            print(c, end='')
