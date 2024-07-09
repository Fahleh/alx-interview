#!/usr/bin/python3
""" Module for Minimum Operations"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to
    result in exactly n H characters.
    """
    # Output must be at least 2 chars (copy all & paste.)
    if (n < 2):
        return 0
    num_of_ops, base_num = 0, 2
    while base_num <= n:
        # While base_num is a factor of n (divides n with no remainder)
        while n % base_num == 0:
            # Incement num_of_ops by base_num
            num_of_ops += base_num
            # set n to the remainder
            n //= base_num
        # If base_num is not a factor, increment it until it becomes one.
        base_num += 1
    return num_of_ops
