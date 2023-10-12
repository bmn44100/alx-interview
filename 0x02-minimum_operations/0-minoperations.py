#!/usr/bin/python3
"""
module for minimum operations
"""


def minOperations(n):
    """method for minimum operations"""
    if n <= 1:
        return 0
    count = 0
    for i in range(2, n):
        while n % i == 0:
            count += i
            n /= i
        ++i
    return count
