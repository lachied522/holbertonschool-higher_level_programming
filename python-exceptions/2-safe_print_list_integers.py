#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0

    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                num_printed += 1
            except ValueError:
                continue
            except TypeError:
                continue

        print("")

        return num_printed
    except Exception as e:
        raise e
