#!/usr/bin/python3

import unittest
import json
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id(self):

        L1 = Base()
        self.assertEqual(L1.id, 1)
        L2 = Base()
        self.assertEqual(L2.id, 2)
        L3 = Base(33)
        self.assertEqual(L3.id, 33)
        L4 = Base()
        self.assertEqual(L4.id, 3)

    def test_instance(self):

        base1 = Base()
        self.assertIsInstance(base1, object)
