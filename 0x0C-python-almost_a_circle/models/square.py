#!/usr/bin/python3
""""""
from models.rectangle import Rectangle
""""""


class Square(Rectangle):

    """ """
    def __init__(self, size, x=0, y=0, id=None):

        """ """
        super().__init__(size, size, x, y, id)

    def __str__(self):

        """ """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):

        """ """
        return self.width

    @size.setter
    def size(self, value):

        """ """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    """................................................................."""

    def update(self, *args, **kwargs):

        """ """
        if len(args) == 0:
            for keywords, value in kwargs.items():
                self.__setattr__(keywords, value)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):

        """ """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "height"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
