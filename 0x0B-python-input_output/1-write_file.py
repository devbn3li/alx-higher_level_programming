#!/usr/bin/python3
"""This defines a file-writing function"""


def write_file(filename="", text=""):
    """
    write string to text file

    Return:
        number of characters written
    """
    with open(filename, 'w') as file:
        return file.write(text)
