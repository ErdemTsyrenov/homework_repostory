"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from collections.abc import Collection
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    elements = []
    if isinstance(tree, dict):
        elements = [tree[key] for key in tree.keys()]
    else:
        elements = tree
    num = 0
    for item in elements:
        if item == element:
            num += 1
        elif isinstance(item, Collection) and not isinstance(item, str):
            num += find_occurrences(item, element)
    return num
