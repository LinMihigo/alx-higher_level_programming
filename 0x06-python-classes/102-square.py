#!/usr/bin/python3
"""Defining the Square class"""

class Square:
    """Description of the Square class

    Args:
        size (int or float): value to set to size attribute

    Attributes:
        __size (int or float): private instance attribute to set
    """
    def __init__(self, size=0):
        """Initialize the square with a size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, ensuring it is a number (int or float) and non-negative.

        Args:
            value (int or float): value to set for size.

        Raises:
            TypeError: if value is not a number.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            float: the area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if the area of the current square is equal to another square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if the area of the current square is not equal to another square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if the area of the current square is less than another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if the area of the current square is less than or equal to another square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if the area of the current square is greater than another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if the area of the current square is greater than or equal to another square."""
        return self.area() >= other.area()
