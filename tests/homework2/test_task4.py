from homework2.task4 import cache


def func(a: int, b: int):
    return (a ** b) ** 2


def test_default():
    cache_func = cache(func)
    some = 100, 200
    val1 = cache_func(*some)
    val2 = cache_func(*some)
    assert val1 is val2


def build_list_range(stop: int):
    return list(range(stop))


def test_own():
    cache_func = cache(build_list_range)
    stop = 10
    a = cache_func(stop)
    b = cache_func(stop)
    assert a is b
