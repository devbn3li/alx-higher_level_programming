#!/usr/bin/python3
"""Contain defin of 'add_attribute' function"""


def add_attribute(obj, name, value):
    """Add new attribute to an object if its possible"""
    if hasattr(obj, '__dict__'):
        obj.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
