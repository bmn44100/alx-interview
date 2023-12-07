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
    sieve = [True for i in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i*i, n + 1, i):
            sieve[j] = False
    sieve[0] = sieve[1] = False
    c = 0
    for i in range(len(sieve)):
        if sieve[i]:
            c += 1
        sieve[i] = c
    p1 = 0
    for n in nums:
        p1 += sieve[n] % 2 == 1
    if p1 * 2 == len(nums):
        return None
    if p1 * 2 > len(nums):
        return "Maria"
    return "Ben"