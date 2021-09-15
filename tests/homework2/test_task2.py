import pytest

from homework2.task2 import major_and_minor_elem


@pytest.mark.parametrize('test_input, expected', [
    ([3, 2, 3], (3, 2)),
    ([2, 2, 1, 1, 1, 2, 2], (2, 1))
])
def test_default(test_input, expected):
    assert major_and_minor_elem(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([0, 0, 1, 0, 0, 1, 0, 0, 0, 3, 2, 3], (0, 2)),
    ([0, 1, 0, 1, 0], (0, 1))
])
def test_with_zeros(test_input, expected):
    assert major_and_minor_elem(test_input) == expected
