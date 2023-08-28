#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    All = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            All += 1
        except IndexError:
            break
    print("")
    return (All)
