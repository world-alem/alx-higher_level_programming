#!/usr/bin/python3
"""3-square"""


class Square:
    """The square class"""

    def __init__(self, size=0):
        """__init__"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size
