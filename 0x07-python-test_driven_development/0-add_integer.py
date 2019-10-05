#!/usr/bin/python3
"""
    module adds two integers (a + b)
        a (int | float)
        b (int | float)
"""


def add_integer(a, b=98):
    """
     Funtion that adds two numbers, the int or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
