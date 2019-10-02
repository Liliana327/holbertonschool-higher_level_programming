#!/usr/bin/python3
""" This function defines a Square

    It will be used by the test file based on 2-square.py

    Example:
        ./2-main.py
"""


class Square:
    """ Creates a class Square which has a size
    """
    def __init__(self, size=0):
        """ Initializes instance attributes
        """
        if not isinstance(size, int):
            raise TypeError('''size must be an integer''')
        if size < 0:
            raise ValueError('''size must be >= 0''')
        self.__size = size

    def area(self):
        """ Gets area of Square
        """
        return self.__size * self.__size
