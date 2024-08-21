#!/usr/bin/python3
"""
Module for make change function
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    Returns: 
      : Fewest number of coins needed to meet total.
      : 0 If total is 0 or less.
      : -1 if otal cannot be met by any number of coins you have.

    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    coins_needed = [float('inf')] * (total + 1)
    coins_needed[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            coins_needed[i] = min(coins_needed[i], coins_needed[i - coin] + 1)

    return coins_needed[total] if coins_needed[total] != float('inf') else -1
