"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from itertools import zip_longest


def apply_backspace(string: str):
    delete_symbol = False
    for char in reversed(string):
        if char == '#':
            delete_symbol = True
        elif delete_symbol:
            delete_symbol = False
            continue
        else:
            yield char


def backspace_compare(first: str, second: str) -> bool:
    for c1, c2 in zip_longest(apply_backspace(first), apply_backspace(second)):
        if c1 != c2:
            return False
    return True
