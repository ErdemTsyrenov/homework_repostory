from homework3.task1 import cache


def test_int_value_cache_two_times():
    num_calls = 0

    @cache(2)
    def f(a, b):
        nonlocal num_calls
        num_calls += 1
        return a, a+b

    some = (1, 2)
    [f(*some) for i in range(4)]
    assert num_calls == 2


def test_int_value_cache_zero_times():
    num_calls = 0

    @cache(0)
    def f(a, b, c='Hello'):
        nonlocal num_calls
        num_calls += 1
        return {a, b, c}

    some = (1, 2)
    [f(*some) for i in range(5)]
    assert num_calls == 5


def test_int_value_cache_three_times():
    num_calls = 0

    @cache(3)
    def f(a, b):
        nonlocal num_calls
        num_calls += 1
        return a**(a+b)

    some = (1, 2)
    [f(*some) for i in range(9)]
    assert num_calls == 3
