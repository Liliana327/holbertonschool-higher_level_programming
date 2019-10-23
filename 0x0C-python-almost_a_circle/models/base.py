#!/usr/bin/python3
"""Module Base
"""


import json
import os


class Base:
    """created class name Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class
            Args:
                id (int): id the class Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the string JSON
            Args:
                list the dictionarie
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Escribe a JSON string 
        """
        filename = '{}.json'.format(cls.__name__)
        dic = []

        if list_objs is not None:
            for i in list_objs:
                dic.append(cls.to_dictionary(i))

        with open(filename, 'w', encoding='utf-8') as new_file:
            new_file.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
            Args:
                json_string: string representing a list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
            Args:
                cls: belonging class
                **dictionary: double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(36916, 36916)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Square":
            dummy = cls(36916)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
            Args:
                cls: belonging class
        """
        filename = '{}.json'.format(cls.__name__)
        list_ins = []

        if os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as new_file:
                content = cls.from_json_string(new_file.read())
            for i in content:
                list_ins.append(cls.create(**i))
            return list_ins
        else:
            return []
