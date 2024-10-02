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
    def size(self):
        """Retrieve __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): value to set to __size.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value (tuple): value to set to __position.

        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the square area

        Returns:
            int: the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#'"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String representation of the square"""
        result = ""
        if self.__size == 0:
            return "\n"
        result += "\n" * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.strip()
