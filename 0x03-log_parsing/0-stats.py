#!/usr/bin/python3

import sys


def custom_print(dict_sc, total_file_size):
    """Method for printing in a particular format."""

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


SIZE = 0
CODE = 0
COUNT = 0
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
        curr_line = line.split()
        stripped_line = curr_line[::-1]

        if len(stripped_line) > 2:
            COUNT += 1

            if COUNT <= 10:
                SIZE += int(stripped_line[0])  # file size
                CODE = stripped_line[1]  # status code

                if (CODE in status_dict):
                    status_dict[CODE] += 1

            if (COUNT == 10):
                custom_print(status_dict, SIZE)
                COUNT = 0

finally:
    custom_print(status_dict, SIZE)
