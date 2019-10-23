#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
import json
import os
import sys
from io import StringIO


class test_rectangle(unittest.TestCase):

    def test_init(self):

        self.r_instance = Rectangle(33, 11)

    def test_del(self):

        r_instance = Rectangle(1, 2)
        del(self.r_instance)

    def test_width_int(self):

        self.r_instance.width = 33
        self.assertEqual(33, self.r_instance.width)

    def test_height_int(self):

        self.r_instance.height = 33
        self.assertEqual(33, self.r_instance.height)

    def test_x_int(self):

        self.r_instance.x = 33
        self.assertEqual(33, self.r_instance.x)

    def test_y_int(self):

        self.r_instance.y = 33
        self.assertEqual(33, self.r_instance.y)

    def test_rectangle_id(self):

        r_instance = Rectangle(33, 1, 2, 3, 4)
        self.assertEqual(4, r_instance.id)

    def test_width_non_int(self):

        with self.assertRaises(TypeError):
            r_instance = ("44", 33, 0)

    def test_height_non_int(self):

        with self.assertRaises(TypeError):
            r_instance = (44, "33", 5, 6)

    def test_x_non_int(self):

        with self.assertRaises(TypeError):
            r_instance = (44, 33, "5", 6)

    def test_y_non_int(self):

        with self.assertRaises(TypeError):
            r_instance(44, 33, 5, "6")

    def test_width_negative(self):

        with self.assertRaises(TypeError):
            r_instance = (-1, 2, 3, 4)

    def test_height_negative(self):

        with self.assertRaises(TypeError):
            r_instance = (2, -3, 4, 5)

    def test_x_negative(self):

        with self.assertRaises(TypeError):
            r_instance = (2, 3, -4, 5)

    def test_y_negative(self):

        with self.assertRaises(TypeError):
            r_instance = (2, 3, 4, -5)

    def test_width_zero(self):

        with self.assertRaises(ValueError):
            r_instance = (0, 1)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            r_instance = (1, 0)

    def test_rectangle_area(self):
        r_instance = Rectangle(3, 5)
        self.assertEqual(r_instance.area(), 3 * 5)

    def test_rectangle_str_overload(self):

        r_instance = Rectangle(1, 2, 3, 4, 33)
        self.assertEqual(r_instance.__str__(), "[Rectangle] (33) 3/4 - 1/2")

    def test_rectangle_update_id(self):

        self.r_instance.update(33)
        self.assertEqual(33, self.r_instance.id)

    def test_rectangle_update_width(self):

        self.r_instance.update(33, 44)
        self.assertEqual(44, self.r_instance.width)

    def test_rectangle_update_height(self):

        self.r_instance.update(33, 44, 55)
        self.assertEqual(55, self.r_instance.height)

    def test_rectangle_update_x(self):

        self.r_instance.update(33, 44, 55, 66)
        self.assertEqual(66, self.r_instance.x)

    def test_rectangle_update_y(self):

        self.r_instance.update(33, 44, 55, 66, 77)
        self.assertEqual(77, self.r_instance.y)

    def test_rectangle_update1(self):

        self.r_instance.update(width=1, id=33, height=2, x=3, y=4)
        self.assertEqual(33, self.r_instance.id)
        self.assertEqual(1, self.r_instance.width)
        self.assertEqual(2, self.r_instance.height)
        self.assertEqual(3, self.r_instance.x)
        self.assertEqual(4, self.r_instance.y)

    def test_rectangle_update2(self):

        self.r_instance.update(5, 7, 9, y=11, height=33)
        self.assertEqual(5, self.r_instance.id)
        self.assertEqual(7, self.r_instance.width)
        self.assertEqual(33, self.r_instance.height)
        self.assertEqual(9, self.r_instance.x)
        self.assertEqual(11, self.r_instance.y)

    def test_to_dictionary(self):
