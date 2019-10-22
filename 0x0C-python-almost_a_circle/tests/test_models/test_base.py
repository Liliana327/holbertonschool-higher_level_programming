#!/usr/bin/python3
'''
Unit tests for Base class
'''
import unittest
from models.base import Base
from models.square import Square
import json


class test_base(unittest.TestCase):
    '''
    Tests for Base
    '''
    def test_id1(self):
        '''
        Testing no id sent
        '''
        i1 = Base()
        self.assertEqual(1, i1.id)

    def test_id2(self):
        '''
        Testing a valid id
        '''
        i1 = Base(33)
        self.assertEqual(33, i1.id)

    def test_id3(self):
        '''
        Testing a negative id
        '''
        i1 = Base(-33)
        self.assertEqual(-33, i1.id)

    def test_id4(self):
        '''
        Testing an id of 0
        '''
        i1 = Base(0)
        self.assertEqual(0, i1.id)

    def test_id5(self):
        '''
        Testing a non-int value for id
        '''
        i1 = Base("hi")
        self.assertEqual("hi", i1.id)

    def test_id5(self):
        '''
        Testing a negative id
        '''
        i1 = Base(-33)
        self.assertEqual(-33, i1.id)

    def test_id6(self):
        '''
        Testing non-int value for id
        '''
        i1 = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], i1.id)

    def test_base1(self):
        '''
        Testing int to JSON string function
        '''
        s1 = Square(33)
        json_obj = s1.to_dictionary()
        converted = Base.to_json_string([json_obj])
        self.assertEqual(type(converted), str)

    def test_base2(self):
        '''
        Testing multiple ints to JSON
        '''
        s1 = Square(33, 11, 9, 10)
        json_obj = s1.to_dictionary()
        converted = Base.to_json_string([json_obj])
        self.assertEqual(converted, [{"id": 33, "size": 11, "x": 9, "y": 10}])

    def test_base3(self):
        '''
        Testing sending None to to_json_string function
        '''
        s1 = Square(33, 11, 9, 10)
        json_obj = s1.to_dictionary()
        converted = Base.to_json_string(None)
        self.assertEqual(converted, "[]")

    def test_id7(self):
        '''
        Testing a dict for id
        '''
        i1 = Base({'id': 33})
        self.assertEqual({'id': 33}, i1.id)

    def test_id8(self):
        '''
        Testing tuple for id
        '''
        i1 = Base((33, 44))
        self.assertEqual((33, 44), i1.id)

    def test_base4(self):
        '''
        Testing an empty list to to_json_string function
        '''
        s1 = Square(33, 11, 9, 10)
        json_obj = s1.to_dictionary()
        converted = Base.to_json_string([])
        self.assertEqual(converted, "[]")
