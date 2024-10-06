#!/usr/bin/python3
"""Define a function adding integers"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Arguments:
    a -- The first number, should be an integer or float.
    b -- The second number, defaults to 98, should be an integer or float.

    Returns:
    The sum of a and b as an integer.

    Raises:
    TypeError -- If a or b are not integers or floats, or if NaN is encountered
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if any(isinstance(x, float) and
           (x != x or x in (float('inf'), float('-inf'))) for x in (a, b)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
