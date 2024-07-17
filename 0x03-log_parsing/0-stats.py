#!/usr/bin/python3

import sys


def custom_print(dict_sc, total_file_size):
    """Method for printing in a particular format."""

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


size = 0
code = 0
count = 0
status_dict = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        curr_line = line.split()  # ✄ trimming
        curr_line = curr_line[::-1]  # inverting

        if len(curr_line) > 2:
            count += 1

            if count <= 10:
                size += int(curr_line[0])  # file size
                code = curr_line[1]  # status code

                if (code in status_dict.keys()):
                    status_dict[code] += 1

            if (count == 10):
                custom_print(status_dict, size)
                count = 0

finally:
    custom_print(status_dict, size)