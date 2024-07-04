#!/usr/bin/python3
"""A module for working with lockboxes."""


def canUnlockAll(boxes):
    """Checks if all the boxes in a list can be openend."""
    num = len(boxes)
    checked = set([0])
    unchecked = set(boxes[0]).difference(set([0]))
    while len(unchecked) > 0:
        box_id = unchecked.pop()
        if not box_id or box_id >= num or box_id < 0:
            continue
        if box_id not in checked:
            unchecked = unchecked.union(boxes[box_id])
            checked.add(box_id)
    return num == len(checked)
