#!/usr/bin/python3

import json

"""Task number 1"""


class Base:

    """ """
    __nb_objects = 0

    def __init__(self, id=None):

        'Instance of the class Base'

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """Task number 14"""

    @staticmethod
    def to_json_string(list_dictionaries):
        """ """

        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    """Task number 15"""

    @classmethod
    def save_to_file(cls, list_objs):

        """ """
        with open("{}.json".format(cls.__name__), mode='w+',
                  encoding='utf-8') as f:
            f.write(cls.to_json_string([cls.to_dictionary(M)
                    for M in list_objs]))

    """Task number 16"""

    @staticmethod
    def from_json_string(json_string):
        """ """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    """Task number 17"""

    @classmethod
    def create(cls, **dictionary):
        """ """

        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            new_instance = Rectangle(1, 2)
        if cls.__name__ == "Square":
            new_instance = Square(1)
        new_instance.update(**dictionary)
        return new_instance

    """Task number 18"""

    @classmethod
    def load_from_file(cls):
        """ """
        try:
            with open('{}.json'.format(cls.__name__), mode='r',
                      encoding='utf-8') as f:
                instance_list = cls.from_json_string(f.read())
        except IOError:
            return []
        return [cls.create(**item) for item in instance_list]
