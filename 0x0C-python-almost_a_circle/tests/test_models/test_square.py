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


class TestSquare(unittest.TestCase):
    """Class for unittests
    """
    def test_id(self):
        """Test id
        """
        Base._Base__nb_objects = 0
        s1 = Square(6, 9)
        self.assertEqual(s1.id, 1)
        s2 = Square(9, 16)
        self.assertEqual(s2.id, 2)
        s3 = Square(6, 9, 16, 33)
        self.assertEqual(s3.id, 33)

    def test_attrs(self):
        """Test attributes
        """
        s = Square(3, 9, 16, 33)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 9)
        self.assertEqual(s.y, 16)
        self.assertEqual(s.id, 33)

    def test_size(self):
        """Test size
        """
        s = Square(6)
        self.assertEqual(s.size, 6)

    def test_x(self):
        """Test x
        """
        s = Square(9, 8, 7)
        self.assertEqual(s.x, 8)

    def test_y(self):
        """Test y
        """
        s = Square(9, 16, 7)
        self.assertEqual(s.y, 7)

    def test_size_TypeError(self):
        """Test size TypeError (size != int)
        """
        self.assertRaises(TypeError, Square, 'hello')

    def test_size_ValueError1(self):
        """Test size ValueError (size = 0)
        """
        self.assertRaises(ValueError, Square, 0)

    def test_size_ValueError2(self):
        """Test size ValueError (size < 0)
        """
        self.assertRaises(ValueError, Square, -3)

    def test_x_TypeError(self):
        """Test x TypeError (x != int)
        """
        self.assertRaises(TypeError, Square, 6, {9}, 9)

    def test_x_ValueError1(self):
        """Test x ValueError (x < 0)
        """
        self.assertRaises(ValueError, Square, 6, -9, 16)

    def test_y_TypeError(self):
        """Test y TypeError (y != int)
        """
        self.assertRaises(TypeError, Square, 6, 9, [16])

    def test_y_ValueError1(self):
        """Test y ValueError (y < 0)
        """
        self.assertRaises(ValueError, Square, 6, 9, -16)

    def test_area(self):
        """Test area
        """
        s1 = Square(6)
        self.assertEqual(s1.area(), 36)
        s2 = Square(9)
        self.assertEqual(s2.area(), 81)

    def test_str(self):
        """Test str
        """
        s1 = Square(16, 6, 3, 33)
        self.assertEqual('[Square] (33) 6/3 - 16', str(s1))
        s2 = Square(3)
        self.assertEqual('[Square] ({}) 0/0 - 3'.format(s2.id), str(s2))

    def test_update_args(self):
        """Test update args
        """
        s = Square(9, 6, 3, 33)
        self.assertEqual(33, s.id)
        self.assertEqual(9, s.size)
        self.assertEqual(6, s.x)
        self.assertEqual(3, s.y)
        s.update(8, 7, 2, 1)
        self.assertEqual(8, s.id)
        self.assertEqual(7, s.size)
        self.assertEqual(2, s.x)
        self.assertEqual(1, s.y)

    def test_update_kwargs(self):
        """Test update kwargs
        """
        s = Square(16, 6, 3, 33)
        s.update(id=6, x=5, size=5)
        self.assertEqual(6, s.id)
        self.assertEqual(5, s.x)
        self.assertEqual(5, s.size)

    def test_dict(self):
        """Test dictionary
        """
        s = Square(9, 6, 3, 33)
        dic = s.to_dictionary()
        self.assertEqual(dic['size'], 9)
        self.assertEqual(dic['x'], 6)
        self.assertEqual(dic['y'], 3)
        self.assertEqual(dic['id'], 33)
