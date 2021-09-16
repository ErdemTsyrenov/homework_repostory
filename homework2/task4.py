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


def merge_args(*args, **kwargs):
    keys = sorted(kwargs.keys())
    for k in keys:
        args.append(kwargs[k])
    return tuple(args)


def cache(f: Callable):
    memory = dict()

    def wrapped(*args, **kwargs):
        arg = merge_args(*args, **kwargs)  # merge into hashable object
        if arg not in memory:
            memory[arg] = f(*args, **kwargs)
        return memory[arg]
    return wrapped
