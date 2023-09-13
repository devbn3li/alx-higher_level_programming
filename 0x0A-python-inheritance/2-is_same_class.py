#!/usr/bin/python3
"""Contain def of 'is_same_class' function"""


def is_same_class(obj, a_class):
    """
    return True if object is exactly an instance of the specified class,
    otherwise False
    """
    return type(obj) == a_class
