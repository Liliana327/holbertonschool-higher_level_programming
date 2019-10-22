#!/usr/bin/python3

import json

"""Task number 1"""

class Base:
    __nb_objects = 0

    def __init__(self, id=None):

        'Instance of the class Base'

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
