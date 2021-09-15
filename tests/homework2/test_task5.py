import string

import pytest

from homework2.task5 import custom_range


@pytest.mark.parametrize('test_input, expected', [
    ([string.ascii_lowercase, 'g'],
     ['a', 'b', 'c', 'd', 'e', 'f']),
    ([string.ascii_lowercase, 'g', 'p'],
     ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']),
    ([string.ascii_lowercase, 'p', 'g', -2],
     ['p', 'n', 'l', 'j', 'h'])
])
def test_default(test_input, expected):
    assert custom_range(*test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([[1, 2, 3, 4], 3], [1, 2]),
    ([(1, 2, 3, 4, 5, 6), 3, 6], [3, 4, 5]),
    ([{(1, 2), (1, 3), (1, 4), (1, 5)}, (1, 4)], [(1, 2), (1, 3)]),
    ([(1, 2, 3, 4, 5, 6), 6, 3, -1], [6, 5, 4])
])
def test_dif_containers_of_integers(test_input, expected):
    assert custom_range(*test_input) == expected
