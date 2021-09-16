from homework2.task4 import cache


def test_default():
    num_calls = 0

    @cache
    def func(a: int, b: int):
        nonlocal num_calls
        num_calls += 1
        return (a ** b) ** 2
    some = 100, 200
    [func(*some) for i in range(10)]
    assert num_calls == 1


def test_own():
    num_calls = 0

    @cache
    def build_list_range(stop: int):
        nonlocal num_calls
        num_calls += 1
        return list(range(stop))
    stop = 10
    [build_list_range(stop) for i in range(100)]
    assert num_calls == 1
