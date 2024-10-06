#!/usr/bin/python3
"""Define a func that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Parameters:
    ----------
    matrix : list of lists
        A matrix (list of lists) containing integers or floats.
        All rows must be of the same size.
    div : int or float
        The number by which to divide all elements of the matrix.

    Returns:
    -------
    list of lists
        A new matrix where each element is divided by div and
        rounded to 2 decimal places.

    Raises:
    ------
    TypeError:
        - If the matrix is not a list of lists of integers or floats.
        - If each row of the matrix is not the same size.
        - If div is not a number (integer or float).
    ZeroDivisionError:
        - If div is zero.
    """
    str = "matrix must be a matrix (list of lists) of integers/floats"
    if not (isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix)):
        raise TypeError(str)

    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError(str)

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
