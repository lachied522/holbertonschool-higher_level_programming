#!/usr/bin/python3
def uppercase(string):
    for i, c in enumerate(string):
        end = '' if i < len(string) - 1 else '\n'
        if ord('a') <= ord(c) and ord(c) <= ord('z'):
            print("{:c}".format(ord(c) - ord('a') + ord('A')), end=end)
        else:
            print(c, end=end)
