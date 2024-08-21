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

    balance = total
    count = 0
    index = 0
    change = sorted(coins, reverse=True)
    n = len(coins)

    while balance > 0:
        if index >= n:
            return -1
        if balance - change[index] >= 0:
            balance -= change[index]
            count += 1
        else:
            index += 1
    return count
