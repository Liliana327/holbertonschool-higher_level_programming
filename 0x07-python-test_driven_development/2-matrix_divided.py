#!/usr/bin/python3
"""
    matrix (int | float)
    div    (int | float)
"""


def matrix_divided(matrix, div):
    """
    Divided elements the matrix
    """
    Error_1 = "matrix must be a matrix (list of lists) of integers/floats"
    Error_2 = "Each row of the matrix must have the same size"
    Error_3 = "div must be a number"
    Error_4 = "division by zero"

    if not isinstance(matrix, list):
        raise TypeError(Error_1)
    if not isinstance(matrix[0], list) and not isinstance(matrix[1], list):
        raise TypeError(Error_1)

    length = len(matrix[0])

    for i in matrix:
        if len(i) != length:
            raise TypeError(Error_2)
        for ele in i:
            if not isinstance(ele, (int, float)):
                raise TypeError(Error_1)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(Error_3)
    if div == 0:
        raise ZeroDivisionError(Error_4)

    return [[round(m / div, 2) for m in i] for i in matrix]
