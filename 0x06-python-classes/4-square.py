#!/usr/bin/python3
"""Defining the Square class"""


class Square:
    """Description of the Square class

    Args:
        size (int): int value to set to attribute

    Attributes:
        __size (int): private instance attribute to set\

    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):  #: retrieve __size
        return self.__size

    @size.setter
    def size(self, value):  #: property setter for size
        """property setter method for size

        Args:
            value (int): value to set __size to.

        """
        if isinstance(value, int):
            if value < 0:
                raise TypeError("size must be >= 0")
            self.__size = value
        else:
            raise ValueError("size must be an integer")

    def area(self):  #: Calculates the square area
        return self.__size * self.__size
