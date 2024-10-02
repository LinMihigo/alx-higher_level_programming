#!/usr/bin/python3
"""Defining the Square class"""


class Square:
    """Description of the Square class

    Args:
        size (int): int value to set to size attribute
        position (tuple): value to set to position attribute

    Attributes:
        size (int): private instance attribute to set
        position (tuple): private instance attribute to set

    """
    def __init__(self, size=0, position=(0, 0)):
        """private instance attributes init"""
        self.size = size
        self.position = position

    @property
    def size(self):  #: retrieve __size
        return self.__size

    @size.setter
    def size(self, value):
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

    @property
    def position(self):  #: retrieve __position
        return self.__position

    @position.setter
    def position(self, value):
        if (len(value) == 2 and isinstance(value, tuple) and
            isinstance(value[0], int) and isinstance(value[1], int) and
            value[0] > 0 and value[1] > 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):  #: Calculates the square area
        return self.__size * self.__size

    def my_print(self):  #: prints to stdout the square with the character '#'
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")
