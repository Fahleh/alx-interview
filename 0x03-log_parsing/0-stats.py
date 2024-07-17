#!/usr/bin/python3
import sys
import signal


def custom_print(dict_sc, total_file_size):
    """Method for printing in a particular format."""
    print(f"File size: {total_file_size}")
    for key, value in sorted(dict_sc.items()):
        if value != 0:
            print(f"{key}: {value}")


def handle_signal(sig, frame):
    """Handle keyboard interrupt."""
    custom_print(status_dict, SIZE)
    sys.exit(0)


signal.signal(signal.SIGINT, handle_signal)

SIZE = 0
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
        tokens = line.split()
        if len(tokens) < 9:
            continue

        try:
            size = int(tokens[-1])
            code = tokens[-2]
        except ValueError:
            continue

        if code in status_dict:
            status_dict[code] += 1

        SIZE += size
        COUNT += 1

        if COUNT % 10 == 0:
            custom_print(status_dict, SIZE)

finally:
    custom_print(status_dict, SIZE)
