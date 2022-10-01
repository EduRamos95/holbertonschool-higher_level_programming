#!/usr/bin/python3
"""
Module 100-append_after
function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Module Search and update
    """
    with open(filename, 'r+', encoding="utf-8") as fd:
        lines = fd.readlines()
        i = 0
        for line in lines:
            if line.find(search_string) != -1:
                lines.insert(i + 1, new_string)
            i += 1
        fd.seek(0)
        fd.write("".join(lines))
