#!/usr/bin/python3
"""5-square"""


class Square:
    """The square class"""

    def __init__(self, size=0):
        """__init__"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def my_print(self):
        """my_print"""
        if (self.__size == 0):
            print()

        for i in range(self.__size):
            [print('#', end='') for j in range(self.__size)]
            print()

    def area(self):
        """area"""
        return self.__size * self.__size
