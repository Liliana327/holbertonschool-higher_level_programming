#!/usr/bin/python3
"""Unittest for Base module
"""


import unittest
import json
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Class for unittests
    """

    def test_id(self):
        """Test id
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(33)
        self.assertEqual(b3.id, 33)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_instance(self):
        """Test instance
        """
        base1 = Base()
        self.assertIsInstance(base1, object)
