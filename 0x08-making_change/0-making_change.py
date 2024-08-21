def makecount(coins, total):
    """
    Given a pile of coins of different values,
    Returns: 
      : Fewest number of coins needed to meet total.
      : 0 If total is 0 or less.
      : -1 if total cannot be met by any number of coins you have.

    """
    if not coins:
        return -1
    if total <= 0:
        return 0
    count = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            count += 1
        if (total == 0):
            return count
    return -1
