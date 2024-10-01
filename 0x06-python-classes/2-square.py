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
        if isinstance(size, int):
            if size < 0:
                raise TypeError("size must be >= 0")
            self.__size = size
        else:
            raise ValueError("size must be an integer")
