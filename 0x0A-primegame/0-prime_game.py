#!/usr/bin/python3
"""
module for prime game
"""


def isWinner(x, nums):
    """
    function to determine who wins the game
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True for i in range(n + 1, 2)]
    for i in range(2, int(n ** 0.5) + 1):
        if not sieve[i]:
            continue
        for j in range(i * i, n + 1, i):
            sieve[j] = False
    sieve[0] = sieve[1] = False
    k = 0
    for i in range(len(sieve)):
        if sieve[i]:
            k += 1
        sieve[i] = k
    player1 = 0
    for n in nums:
        player1 += sieve[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"