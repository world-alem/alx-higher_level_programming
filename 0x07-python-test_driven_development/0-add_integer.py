#!/usr/bin/python3
"""
    Integer addition
"""


def add_integer(a, b=98):
    """Adds two integers"""

    if type(a) not in [int, float]:
        raise TypeError('TypeError: a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('TypeError: b must be an integer')

    return int(a) + int(b)
