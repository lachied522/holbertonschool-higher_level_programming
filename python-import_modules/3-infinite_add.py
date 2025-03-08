#!/usr/bin/python3
import sys


def add_args():
    s = 0

    for i in range(1, len(sys.argv)):
        s += int(sys.argv[i])

    print(s)


if __name__ == "__main__":
    add_args()
