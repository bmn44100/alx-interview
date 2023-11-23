#!/usr/bin/python3

"""
module for making change
"""

def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine
    the fewest number of coins needed to meet a given amount total.
    """

    coins_change = 0
    current_coin = 0

    if total > 0:
        coins = reversed(sorted(coins))

        for coin in coins:
            while current_coin + coin <= total:
                coins_change += 1
                current_coin += coin

            if current_coin != total:
                return -1
    
    return coins_change