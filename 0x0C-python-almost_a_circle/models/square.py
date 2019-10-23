#!/usr/bin/python3
'''
Creates Square class that inherits from Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class that inherits from class Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializes a Square
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        Overloading the __str__ method
        '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        '''
        Getter for private instance attribute size
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        Setter for private instance attribute size

        Args:
            value (int): the value size is being set to
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

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
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        '''
        Returns a dictionary representation of Square
        '''
        return {'id': getattr(self, "id"),
                'size': getattr(self, "height"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
