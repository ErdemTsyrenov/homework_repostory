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
from typing import Callable


@dataclass
class Arg_times:
    arg: tuple
    times: int


def cache(times=1):

    def wrapped(f: Callable):
        memory = []

        def inner(*args, **kwargs):
            if args\
                    not in memory or memory[args][1] == 0:
                memory[args] = [f(*args), times]
            else:
                memory[args][1] -= 1
            return memory[args][0]
        return inner
    return wrapped
