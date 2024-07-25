#!/usr/bin/python3
"""Module for UTF-8 validation."""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    bytes_to_skip = 0  # Num of bytes to skip after a multi-byte char is found
    data_len = len(data)  # Length of the input data list
    for i in range(data_len):
        if bytes_to_skip > 0:
            bytes_to_skip -= 1
            continue

        # Check that current byte is a valid integer & in the range of a byte
        if not isinstance(data[i], int) or data[i] < 0 or data[i] > 0x10FFFF:
            return False

        elif data[i] <= 0x7f:
            # 1-byte character (ASCII)

            bytes_to_skip = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding

            span = 4
            if data_len - i >= span:
                next_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_bytes):
                    return False
                bytes_to_skip = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-byte character
            span = 3
            if data_len - i >= span:
                # Check the next 2 bytes
                next_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_bytes):
                    return False
                bytes_to_skip = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            if data_len - i >= span:
                # Check the next byte
                next_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_bytes):
                    return False
                bytes_to_skip = span - 1
            else:
                return False
        else:
            return False
    return True
