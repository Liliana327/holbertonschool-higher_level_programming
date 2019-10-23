#!/usr/bin/python3

""""""
from models.base import Base
""""""

"""Task number 2"""


class Rectangle(Base):

    """ """
    def __init__(self, width, height, x=0, y=0, id=None):

        'Initializes Rectangle'
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Task number 3"""

    @property
    def width(self):

        """ """
        return self.__width

    @width.setter
    def width(self, value):

        """ """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):

        """ """
        return self.__height

    @height.setter
    def height(self, value):

        """ """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):

        """ """
        return self.__x

    @x.setter
    def x(self, value):

        """ """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ """
        return self.__y

    @y.setter
    def y(self, value):

        """ """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """Task number 4"""

    def area(self):

        """ """
        return self.width * self.height

    """Task number 5"""

    def display(self):

        """ """
        for M in range(self.y):
            print()
        for M in range(self.height):
            for N in range(self.width + self.x):
                if N >= self.x:
                    print('#', end='')
                else:
                    print(' ', end='')
            print()

    """Task number 6"""

    def __str__(self):

        """ """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
    """Task number 7 and 8"""

    def update(self, *args, **kwargs):

        """ """
        if len(args) == 0:
            for keywords, value in kwargs.items():
                self.__setattr__(keywords, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    """Task number 12"""

    def to_dictionary(self):

        """ """
        return {'id': getattr(self, "id"),
                'width': getattr(self, "width"),
                'height': getattr(self, "height"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
