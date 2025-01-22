#!/usr/bin/python3

def best_score(a_dictionary):
    best_value = None
    best_key = None

    if a_dictionary == None:
        return None

    for key in a_dictionary:
        if best_value == None or a_dictionary[key] > best_value:
            best_value = a_dictionary[key]
            best_key = key

    return key
