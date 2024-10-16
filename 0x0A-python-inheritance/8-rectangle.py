#!/usr/bin/python3
"""Importing BaseGeometry and defining the Rectangle Classes"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
    -----------
    width: int
        The width of the rectangle, must be a positive integer.
    height: int
        The height of the rectangle, must be a positive integer.

    Methods:
    --------
    area():
        Calculates and returns the area of the rectangle.
    """

    def __init__(self, width, height):
        """
        Instantiates a rectangle with width and height.

        Parameters:
        -----------
        width: int
            The width of the rectangle, must be a positive integer.
        height: int
            The height of the rectangle, must be a positive integer.

        Raises:
        -------
        TypeError:
            If width or height is not an integer.
        ValueError:
            If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        --------
        int
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height
