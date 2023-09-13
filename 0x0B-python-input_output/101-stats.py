#!/usr/bin/python3
"""This read from standard input and computes metrics
After every 10 lines or the input of a keyboard interruption (CTRL + C),
print following statistics:
    * The total file size up to that point
    * Count of read status codes up to that point
"""


def print_stats(size, status_code):
    """This print accumulated metrics
    Args:
        size (int): This is the accumulated read file size
        status_codes (dict): This is the accumulated count of status codes
    """
    print("File size: {}".format(size))
    for key in sorted(status_code):
        print("{}: {}".format(key, status_code[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_code = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_code)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_code.get(line[-2], -1) == -1:
                        status_code[line[-2]] = 1
                    else:
                        status_code[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_code)

    except KeyboardInterrupt:
        print_stats(size, status_code)
        raise
