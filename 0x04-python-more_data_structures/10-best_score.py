#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    keys = list(a_dictionary.keys())

    my_key = keys[0]
    num = a_dictionary[my_key]

    for key in keys:
        if a_dictionary[key] > num:
            num = a_dictionary[key]
            my_key = key

    return my_key
