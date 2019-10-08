#!/usr/bin/python3
'''
class Rectangle that defines a by: (based on 2-rectangle.py)
'''


class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        return self.width * self.height

    def perimeter(self):

        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):

        symbol = str(self.print_symbol)
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for a in range(self.height - 1):
            string += symbol * self.width + '\n'
        string += symbol * self.width
        return string

    def __repr__(self):
        esto0 = self.__class__.__name__
        esto1 = "{}({}, {})".format(esto0, self.width, self.height)
        string = esto1
        return string

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
