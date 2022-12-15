#!/usr/bin/python3
"""
    this should ba a documentation
"""


class Base:
    """base class"""

    __nb_objects = 0

    def __init(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
