#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    i = 0
    j = 0

    for tup in my_list:
        i += tup[0] * tup[1]
        j += tup[1]

    return (i / j)
