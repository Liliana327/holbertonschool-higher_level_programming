#!/usr/bin/python3
"""Unittest for Rectangle module
"""


import unittest
import json
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Class for unittests
    """
    def test_id(self):
        """Test id
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(6, 9)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(9, 16)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(3, 6, 9, 16, 33)
        self.assertEqual(r3.id, 33)

    def test_attrs(self):
        """Test attributes
        """
        r = Rectangle(3, 6, 9, 16, 33)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 16)
        self.assertEqual(r.id, 33)

    def test_width(self):
        """Test width
        """
        r = Rectangle(6, 9)
        self.assertEqual(r.width, 6)

    def test_height(self):
        """Test height
        """
        r = Rectangle(6, 9)
        self.assertEqual(r.height, 9)

    def test_x(self):
        """Test x
        """
        r = Rectangle(9, 16, 8, 7)
        self.assertEqual(r.x, 8)

    def test_y(self):
        """Test y
        """
        r = Rectangle(9, 16, 8, 7)
        self.assertEqual(r.y, 7)

    def test_width_TypeError(self):
        """Test width TypeError (width != int)
        """
        self.assertRaises(TypeError, Rectangle, '3', 6)

    def test_width_ValueError1(self):
        """Test width ValueError (width = 0)
        """
        self.assertRaises(ValueError, Rectangle, 0, 3)

    def test_width_ValueError2(self):
        """Test width ValueError (width < 0)
        """
        self.assertRaises(ValueError, Rectangle, -3, 3)

    def test_height_TypeError(self):
        """Test height TypeError (height != int)
        """
        self.assertRaises(TypeError, Rectangle, 6, 'hello')

    def test_height_ValueError1(self):
        """Test height ValueError (height = 0)
        """
        self.assertRaises(ValueError, Rectangle, 3, 0)

    def test_height_ValueError2(self):
        """Test height ValueError (height < 0)
        """
        self.assertRaises(ValueError, Rectangle, 3, -3)

    def test_x_TypeError(self):
        """Test x TypeError (x != int)
        """
        self.assertRaises(TypeError, Rectangle, 3, 6, {9}, 9)

    def test_x_ValueError1(self):
        """Test x ValueError (x < 0)
        """
        self.assertRaises(ValueError, Rectangle, 3, 6, -9, 16)

    def test_y_TypeError(self):
        """Test y TypeError (y != int)
        """
        self.assertRaises(TypeError, Rectangle, 3, 6, 9, [16])

    def test_y_ValueError1(self):
        """Test y ValueError (y < 0)
        """
        self.assertRaises(ValueError, Rectangle, 3, 6, 9, -16)

    def test_area(self):
        """Test area
        """
        r1 = Rectangle(6, 9)
        self.assertEqual(r1.area(), 54)
        r2 = Rectangle(9, 16)
        self.assertEqual(r2.area(), 144)
        r3 = Rectangle(3, 6, 9, 16, 33)
        self.assertEqual(r3.area(), 18)

    def test_str(self):
        """Test str
        """
        r = Rectangle(16, 9, 6, 3, 33)
        self.assertEqual('[Rectangle] (33) 6/3 - 16/9', str(r))
        r = Rectangle(3, 6)
        self.assertEqual('[Rectangle] ({}) 0/0 - 3/6'.format(r.id), str(r))

    def test_update_args(self):
        """Test update args
        """
        r = Rectangle(16, 9, 6, 3, 33)
        self.assertEqual(33, r.id)
        self.assertEqual(16, r.width)
        self.assertEqual(9, r.height)
        self.assertEqual(6, r.x)
        self.assertEqual(3, r.y)
        r.update(8, 4, 7, 2, 1)
        self.assertEqual(8, r.id)
        self.assertEqual(4, r.width)
        self.assertEqual(7, r.height)
        self.assertEqual(2, r.x)
        self.assertEqual(1, r.y)

    def test_update_kwargs(self):
        """Test update kwargs
        """
        r = Rectangle(16, 9, 6, 3, 33)
        r.update(id=6, x=5, height=5)
        self.assertEqual(6, r.id)
        self.assertEqual(5, r.x)
        self.assertEqual(5, r.height)

    def test_dict(self):
        """Test dictionary
        """
        r = Rectangle(16, 9, 6, 3, 33)
        dic = r.to_dictionary()
        self.assertEqual(dic['width'], 16)
        self.assertEqual(dic['height'], 9)
        self.assertEqual(dic['x'], 6)
        self.assertEqual(dic['y'], 3)
        self.assertEqual(dic['id'], 33)
