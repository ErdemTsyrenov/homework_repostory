import string
from homework2.task5 import custom_range


def test_default():
    assert custom_range(string.ascii_lowercase, 'g') == \
           ['a', 'b', 'c', 'd', 'e', 'f']
    assert custom_range(string.ascii_lowercase, 'g', 'p') == \
           ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) ==\
           ['p', 'n', 'l', 'j', 'h']


def test_own():
    assert custom_range([1, 2, 3, 4], 3) == [1, 2]
    assert custom_range((1, 2, 3, 4, 5, 6), 3, 6) == \
           [3, 4, 5]
    assert custom_range({(1, 2), (1, 3), (1, 4), (1, 5)}, (1, 4)) == \
           [(1, 2), (1, 3)]
    assert custom_range((1, 2, 3, 4, 5, 6), 6, 3, -1) == \
           [6, 5, 4]
