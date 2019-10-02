#!/usr/bin/python3
""" This function defines a Square
    It will be used by the test file based on 3-square.py
    Example:
        ./3-main.py
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

    @property
    def size(self):
        """retrieve it
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set it
        """
        if not isinstance(value, int):
            raise TypeError('''size must be an integer''')
        if value < 0:
            raise ValueError('''size must be >= 0''')
        self.__size = value

    def area(self):
        """ Gets area of Square
        """
        return self.__size * self.__size

    def my_print(self):
        """hola
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                for m in range(self.__size):
                    print("#", end="")
                print()
