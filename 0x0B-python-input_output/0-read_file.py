#!/usr/bin/python3
"""This define text file-reading function"""


def read_file(filename=""):
    """Read text file UTF8 and print it to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
