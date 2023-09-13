#!/usr/bin/python3
"""Contain definition of 'append_after' func"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
