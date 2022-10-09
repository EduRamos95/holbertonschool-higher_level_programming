#!/usr/bin/python3
"""
module - 101-locked_class
Defines class with no class or object attribute
Control dynamically created instance attributes
"""


class LockedClass:
    """
    prevents user from creating a new instance attribute
    dynamically unless attribute is "first_name"
    """

    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """ initialize the data with the name """
        self.first_name = first_name
