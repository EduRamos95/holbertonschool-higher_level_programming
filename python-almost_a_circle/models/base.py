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
        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']
        matrix = []
        if list_objs is None or len(list_objs) == 0:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dict[:])
        with open(filename, "w") as fd:
            writer = csv.writer(fd)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """
        Method that loads a CSV file
        """
        filename = "{}.csv".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        with open(filename, 'r') as fd:
            reader = csv.reader(fd)
            csv_list = list(reader)
        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            list_keys = ['id', 'size', 'x', 'y']
        matrix = []
        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)
        list_ins = []
        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))
        return list_ins
