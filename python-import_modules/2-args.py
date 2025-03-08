#!/usr/bin/python3
import sys


def print_args():
    n = len(sys.argv) - 1

    if n == 0:
        print("0 arguments.")
        return

    if n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))

    for i in range(1, n + 1):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    print_args()
