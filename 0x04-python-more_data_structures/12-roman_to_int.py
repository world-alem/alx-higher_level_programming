#!/usr/bin/python3
def roman_to_int(roman_string):
    list = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    i = 0
    sum = 0
    if isinstance(roman_string, str):
        for i in range(len(roman_string) - 1):
            if list[roman_string[i]] >= list[roman_string[i + 1]]:
                sum += list[roman_string[i]]
            else:
                sum -= list[roman_string[i]]
            i += 1
        sum += list[roman_string[i]]
        return sum
    return 0
