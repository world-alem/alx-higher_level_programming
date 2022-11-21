#!/usr/bin/python3
"""6-square"""


class Square:
    """The square class"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if (type(position) is not tuple or
                len(position) != 2 or
                not all([type(num) is int and num >= 0 for num in position])):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (type(position) is not tuple or
                len(position) != 2 or
                not all([type(num) is int and num >= 0 for num in position])):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def my_print(self):
        """my_print"""
        if (self.__size == 0):
            print()
            return

        [print() for i in range(self.__position[1])]

        for i in range(self.__size):
            [print(' ', end='') for j in range(self.__position[0])]
            [print('#', end='') for k in range(self.__size)]
            print()

    def area(self):
        """area"""
        return self.__size * self.__size
