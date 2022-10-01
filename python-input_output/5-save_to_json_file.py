#!/usr/bin/python3
"""
Module 5-save_to_json_file
Contains function that writes Python obj to file using JSON represenation
"""


def save_to_json_file(my_obj, filename):
    """
    Writes Python obj to file using JSON represenation
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as fd:
        json.dump(my_obj, fd)
# or you can use: fd.write(json.dump(my_obj))
# if not necesary to use: fd.close() because open it's using "with"
