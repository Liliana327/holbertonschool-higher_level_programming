#!/usr/bin/python3
'''
Creates a Base class to be used for the entire project
'''
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes an instance of class Base
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Converting a dictionary to a JSON string

        Args:
            list_dictionaries (dict): the dictionary to be converted
        '''
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writing the JSON string representation of a list of objects to a file

        Args:
            list_objs (list): list of objects to be converted
        '''
        with open("{}.json".format(cls.__name__), mode='w+',
                  encoding='utf-8') as f:
            f.write(cls.to_json_string([cls.to_dictionary(i)
                    for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns the list representation of a JSON string
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns an instance with all the attributes set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            new_instance = Rectangle(1, 2)
        if cls.__name__ == "Square":
            new_instance = Square(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        '''
        Loads a list of instances from a file

        Args:
            cls: the current class
        '''
        try:
            with open('{}.json'.format(cls.__name__), mode='r',
                      encoding='utf-8') as f:
                instance_list = cls.from_json_string(f.read())
        except IOError:
            return []
        return [cls.create(**item) for item in instance_list]
