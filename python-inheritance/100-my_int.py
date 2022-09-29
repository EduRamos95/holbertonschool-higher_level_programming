#!/usr/bin/python3
"""
Module 100-my_int

Contains class MyInt that inherits from int
Sneaky --> has == and != operators inverted!
"""


class MyInt(int):
    """
    Rebel Version of integer.
    """
    def __init__(self, data1):
        self.data = data1

    def __eq__(self, other):
        return self.data != other

    def __ne__(self, other):
        return self.data == other
