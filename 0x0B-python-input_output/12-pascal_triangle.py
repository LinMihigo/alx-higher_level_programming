#!/usr/bin/python3
"""Defines the pascal_triangle function"""



def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of height n.

    Args:
        n (int): The height of Pascal's triangle.

    Returns:
        list: A list of lists containing the integers of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    return triangle
