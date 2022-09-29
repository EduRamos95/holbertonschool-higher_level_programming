#!/usr/bin/python3
"""
Module 0-lookup
Contains method lookup that returns list of object's attribute and methods
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
