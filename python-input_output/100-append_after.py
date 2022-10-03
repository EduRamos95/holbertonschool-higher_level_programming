#!/usr/bin/python3
"""
Module 100-append_after
function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """appends "new_string" after a line containing
    "search_string" in "filename" """
    with open(filename, 'r+', encoding='utf-8') as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
        f.seek(0)
        f.writelines(line_list)
