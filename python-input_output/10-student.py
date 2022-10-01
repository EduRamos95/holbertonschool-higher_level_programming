#!/usr/bin/python3
"""
Module 10-student
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

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        (list, dictionary, dictionary, string)
        for JSON serialization of an object
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    dic[attr] = self.__dict__[attr]
            return dic
