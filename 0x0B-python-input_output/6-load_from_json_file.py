#!/usr/bin/python3
"""This define JSON file-reading function"""
import json


def load_from_json_file(filename):
    """This create Python object from a JSON file"""
    with open(filename) as file:
        return json.load(file)
