#!/usr/bin/python3
"""Defining BaseGeometry class"""


class BaseGeometry:
    """
    A class intended to represent basic geometric structures.

    Methods:
    --------
    area():
        Raises an Exception to indicate that the area method is not yet
        implemented.
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
