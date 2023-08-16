#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    ls_keys = list(a_dictionary.keys())

    for x in ls_keys:
        num += 1

    return (num)
