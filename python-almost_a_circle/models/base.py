#!/usr/bin/python3
"""
Module Base
T1: Contains private class __nb_objects, and class constructor __init__
T15: adding static method 'def to_json_string(list_dictionaries)'
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
