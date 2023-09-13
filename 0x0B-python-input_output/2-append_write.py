#!/usr/bin/python3
"""This define a file-appending function"""


def append_write(filename="", text=""):
    """
    append string at the end of the text file

    Return:
        the number of characters added
    """
    with open(filename, 'a') as file:
        return file.write(text)
