#!/usr/bin/env python3
add = __import__("0-add").add

a = 1
b = 2

print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
