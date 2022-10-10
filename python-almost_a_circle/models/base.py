#!/usr/bin/python3
"""
Module Base
T1: Contains private class __nb_objects, and class constructor __init__
T15: adding static method 'def to_json_string(list_dictionaries)'
T16: adding class method 'def save_to_file(cls, list_objs)'
T17: adding static method 'def from_json_string(json_string)'
T18: adding class method 'def create(cls, **dictionary)'
T19: adding class method 'def load_from_file(cls)'
T20: adding class method 'def save_to_file_csv(cls, list_objs)'
T20: adding class method 'def load_from_file_csv(cls)'
"""
import json
import os.path
import csv


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
        def create(cls, **dictionary):
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

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attribute already set
        """
        if cls.__name__ == "Rectangle":
            simple_create = cls(1, 1)
        elif cls.__name__ == "Square":
            simple_create = cls(1)
        simple_create.update(**dictionary)
        return (simple_create)

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        with open(filename, "r") as fd:
            list_str = fd.read()
            list_cls = cls.from_json_string(list_str)
            list_to_load = []
            for i in range(len(list_cls)):
                list_to_load.append(cls.create(**list_cls[i]))
            return (list_to_load)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Method that saves a CSV file
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline='') as fd:
            writer = csv.writer(fd)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Method that loads a CSV file
        """
        objs = []
        filename = "{}.csv".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        with open(filename, 'r', newline='') as fd:
            reader = csv.reader(fd)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                o = cls.create(**dic)
                objs.append(o)
        return objs
