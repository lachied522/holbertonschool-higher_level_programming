#!/usr/bin/python3

char_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    reversed_string = roman_string[::-1]

    num = char_map[reversed_string[0]]
    last_char = reversed_string[0]

    for c in reversed_string[1:]:
        if char_map[c] < char_map[last_char]:
            num -= char_map[c]
        else:
            num += char_map[c]
            last_char = c

    return num
