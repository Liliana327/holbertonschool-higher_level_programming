#!/usr/bin/python3
'''
Creates a Rectangle class that inherits from Base
'''
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializes Rectangle
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Getter for private instance attribute width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for private instance attribute width

        Args:
            value (int): the value of the width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Getter for private instance attribute height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for private instance attribute height

        Args:
            value (int): the value of the height
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        Getter from private instance attribute x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for private instance attribute x

        Args:
            value (int): the value of x
        '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        Getter for private instance attribute y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter for private instance attribute y

        Args:
            value (int): the value of y
        '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Calculates the area of a rectangle
        '''
        return self.width * self.height

    def display(self):
        '''
        Prints the rectangle based on numbers given to the rectangle
        '''
        printing = ''
        print('\n' * self.y, end='')
        for i in range(self.height):
            printing += (' ' * self.x) + ('#' * self.width) + '\n'
        print(printing, end='')

    def __str__(self):
        '''
        Updates the class by overloading the __str__ method
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''
        Class method to update the class Rectangle

        Args:
            args: the list of non-keyword arguments to be updated
            kwargs: the list of keyword arguments to be updated
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''
        Returns a dictionary representation of Rectangle
        '''
        return {'id': getattr(self, "id"),
                'width': getattr(self, "width"),
                'height': getattr(self, "height"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
