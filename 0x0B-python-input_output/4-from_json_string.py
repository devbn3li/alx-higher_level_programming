#!/usr/bin/python3
"""This define JSON-to-object function"""
import json


def from_json_string(my_str):
    """This return Python object representation of JSON string"""
    return json.loads(my_str)
