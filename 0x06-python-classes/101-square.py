#!/usr/bin/python3
"""Square"""


class Square:
    """the square class"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        Args:
                size (int): size of the square
                position (tuple): position of the square

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple) or
            len(position) != 2 or
                not all((
                    [isinstance(num, int) and num >= 0 for num in position]
                ))):
            raise TypeError('position must be a tuple of 2 positive integer')
        self.__position = position

    def area(self):
        """returns area"""
        return self.size**2

    def my_print(self):
        """my_print"""
        print(self.__str__())

    def __str__(self):
        """__str__"""
        if (self.__size == 0):
            return ''

        str = ''

        for i in range(self.__position[1]):
            str += '\n'

        for i in range(self.__size):
            for j in range(self.__position[0]):
                str += ' '
            for j in range(self.__size):
                str += '#'
            str += '\n'
        return str
