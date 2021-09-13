"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from collections import defaultdict
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    elem_count = defaultdict(int)
    for elem in inp:
        elem_count[elem] += 1
    minor = inp[0]
    major = inp[0]
    for elem in elem_count:
        if elem_count[elem] < elem_count[minor]:
            minor = elem
        if elem_count[elem] > len(inp) // 2:
            major = elem
    return (major, minor)
