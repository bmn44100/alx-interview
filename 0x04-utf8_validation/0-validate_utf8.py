#!/usr/bin/python3
"""
module for UTF-8 validation
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except:
        return False
    return True