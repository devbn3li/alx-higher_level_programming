#!/usr/bin/python3
"""Contain def of 'inherits_from' function"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance
    of a class that inherited from specified class,
    otherwise False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
