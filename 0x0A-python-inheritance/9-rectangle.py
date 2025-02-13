#!/usr/bin/python3
"""Defining BaseGeometry and Rectangle Classes"""


class BaseGeometry:
    """
    A class intended to represent basic geometric structures.

    Methods:
    --------
    area():
        Raises an Exception to indicate that the area method is not yet
        implemented.

    integer_validator(name, value):
        Validates that the value is an integer and greater than 0.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.

        Raises:
        -------
        Exception:
            With the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer greater than 0.

        Parameters:
        -----------
        name: str
            The name of the value being validated. Assumed to be a string.
        value: Any
            The value to be validated.

        Raises:
        -------
        TypeError:
            If the value is not an integer, with the message '<name> must be an
            integer'.

        ValueError:
            If the value is less than or equal to 0, with the message '<name>
            must be greater than 0'.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
    __str__():
        Returns a string representation of the rectangle.
    __repr__():
        Returns a detailed string representation of the rectangle.
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
        self.__width = width  # Private attribute
        self.integer_validator("height", height)
        self.__height = height  # Private attribute

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        --------
        int
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        --------
        str
            A string in the format: [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        Returns a detailed string representation of the rectangle.

        Returns:
        --------
        str
            A string representation of the rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"
