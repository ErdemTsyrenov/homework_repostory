"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def is_list_or_tuple_or_set(obj):
    return isinstance(obj, list) or \
           isinstance(obj, tuple) or \
           isinstance(obj, set)


def find_occurrences_in_list_tuple_set(iterable, element):
    num = 0
    for item in iterable:
        if item == element:
            num += 1
        elif isinstance(item, dict):
            num += find_occurrences(item, element)
        elif is_list_or_tuple_or_set(item):
            num += find_occurrences_in_list_tuple_set(item, element)
    return num


def find_occurrences(tree: dict, element: Any) -> int:
    num = 0
    for key in tree:
        if tree[key] == element:
            num += 1
        elif isinstance(tree[key], dict):
            num += find_occurrences(tree[key], element)
        elif is_list_or_tuple_or_set(tree[key]):
            num += find_occurrences_in_list_tuple_set(tree[key], element)
    return num
