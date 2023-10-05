#!/usr/bin/python3
"""
module for lockboxes problem
"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened
    """
    def canUnlockAll(boxes):
    locked_boxes = [0]
    for id, box_list in enumerate(boxes):
        if not box_list:
            continue
        for box_key in box_list:
            if box_key < len(boxes) and box_key not in locked_boxes and box_key != id:
                locked_boxes.append(box_key)
    if len(locked_boxes) == len(boxes):
        return True
    return False
