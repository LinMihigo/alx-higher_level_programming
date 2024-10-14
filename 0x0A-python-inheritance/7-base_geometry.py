#!/usr/bin/python3
"""Defining BaseGeometry Class"""


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
        Raises an Exception indicating that the area method is not implemented

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
            If the value is not an integer, with the message '<name> must be
            an integer'.

        ValueError:
            If the value is less than or equal to 0, with the message '<name>
            must be greater than 0'.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
