#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """the initializer"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2*self.width + 2*self.height)

    def my_print(self):
        """print the rectangle with #"""
        if self.width == 0:
            return ''

        str = []
        for i in range(self.height):
            for j in range(self.width):
                str.append('#')
            if i < self.height-1:
                str.append('\n')
        return ''.join(str)

    def __str__(self):
        return self.my_print()
