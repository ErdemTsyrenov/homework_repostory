"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Callable


def in_list(elem, List):
    for item in List:
        if item[0] == elem:
            return True
    return False

def cache(func: Callable) -> Callable:
    memory = []

    def inner(*args, **kwargs):
        if not in_list((args, kwargs), memory):
            memory.append(((args, kwargs), func(*args, **kwargs)))
        for elem in memory:
            if elem[0] == (args, kwargs):
                return elem[1]
    return inner
