#!/usr/bin/python3
"""
Module Base
T1: Contains private class __nb_objects, and class constructor __init__
T15: adding static method 'def to_json_string(list_dictionaries)'
T16: adding class method 'def save_to_file(cls, list_objs)'
T17: adding static method 'def from_json_string(json_string)'
"""
import json


class Base():
    """
    Class Attributes:
        __nb_objects = 0
    Class constructor:
        def __init__(self, id=None):
    Static method:
        def to_json_string(list_dictionaries):
        def from_json_string(json_string):
    Class method:
        def save_to_file(cls, list_objs):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save json strings of all instances into file
        """
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(cls.to_dictionary(obj))
        with open(filename, "w", encoding="utf-8") as fd:
            fd.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        return python obj of JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return (json.loads(json_string))
