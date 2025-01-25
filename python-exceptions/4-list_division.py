#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(max(len(my_list_1), len(my_list_2))):
        num = 0

        try:
            a, b = my_list_1[i], my_list_2[i]
            num = a / b
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(num)

    return result
