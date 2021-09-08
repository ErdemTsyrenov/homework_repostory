from homework3.task1 import cache


def test_int_value_cache_two_times():
    @cache(2)
    def f(a, b):
        return (a, b)

    some = (1, 2)
    res1 = f(*some)
    res2 = f(*some)
    res3 = f(*some)
    res4 = f(*some)
    res5 = f(*some)
    assert res1 is res2
    assert res2 is res3
    assert not (res3 is res4)
    assert res4 is res5


def test_int_value_cache_zero_times():
    @cache(0)
    def f(a, b):
        return {a, b}

    some = (1, 2)
    res1 = f(*some)
    res2 = f(*some)
    res3 = f(*some)
    res4 = f(*some)
    res5 = f(*some)
    assert not (res1 is res2)
    assert not (res2 is res3)
    assert not (res3 is res4)
    assert not (res4 is res5)
