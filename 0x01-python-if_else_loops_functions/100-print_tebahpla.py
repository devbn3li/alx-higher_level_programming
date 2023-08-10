#!/usr/bin/python3
for x in range(122, 96, -1):
    x = x if x % 2 == 0 else x - 32
    print("{:c}".format(x), end="")
