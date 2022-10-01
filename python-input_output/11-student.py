#!/usr/bin/python3
"""
Module 11-student
Contains class Student
that initializes public instance attributes first_name, last_name, and age,
and has public method to_json that retrieves its dictionary representationi
of requested attributes or all if none were requested
"""


class Student():
    """
    Attributes: first_name; last_name; age
    Methods: to_json: retrieves it's dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        """
        Returns dictionary description with simple data structure
        (list, dictionary, dictionary, string)
        for JSON serialization of an object
        """
        if attributes is None:
            return self.__dict__
        else:
            dic = {}
            for attr in attributes:
                if attr in self.__dict__.keys():
                    dic[attr] = self.__dict__[attr]
            return dic

    def reload_from_json(self, json):
        """
        Return: transfer all attributes of jsno to self
        """
        for k, v in json.items():
            setattr(self, k, v)
