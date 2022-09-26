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

    __slots__ = "first_name"
