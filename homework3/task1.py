"""
In previous homework task 4, you wrote a cache function that remembers
other function output value. Modify it to be a parametrized decorator,
so that the following code:

@cache(times=3)
def some_function():
    pass

Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')

>>> f()
? 1
'1'
>>> f()     # will remember previous value
'1'
>>> f()     # but use it up to two times only
'1'
>>> f()
? 2
'2'
"""
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class MemoryItem:
    def __init__(self, val=None, times=None):
        self.val = val
        self.times = times

    val: Any
    times: int


def is_cached(arg, memory):
    if arg in memory and memory[arg].times != 0:
        return True
    else:
        return False


def merge_args(*args, **kwargs):
    keys = sorted(kwargs.keys())
    for k in keys:
        args.append(kwargs[k])
    return tuple(args)


def cache(times=1):

    def wrapped(f: Callable):
        memory = dict()

        def inner(*args, **kwargs):
            arg = merge_args(*args, **kwargs)   # merge into hashable object
            if not is_cached(arg, memory):
                memory[arg] = MemoryItem(val=f(*args, **kwargs),
                                         times=times)
            else:
                memory[arg].times -= 1
            return memory[arg].val
        return inner
    return wrapped
