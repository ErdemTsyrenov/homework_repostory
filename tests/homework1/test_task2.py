import pytest

from homework1.task2 import check_fibonacci


@pytest.mark.parametrize('test_input, expected', [
        ([1, 1, 2, 3, 5, 8, 13], True),
        ([1, 2, 3, 4, 5], False),
        ([3, 5, 8, 13, 21], True),
        ([1, 2, 3, 5], True)
])
def test_data_with_len_more_than_4(test_input, expected):
    assert check_fibonacci(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
        ([], False),
        ([9], False),
        ([1, 2], True),
        ([0], True),
        ([1, 1], True),
        ([1, 1, 2], True),
        ([1], True),
        ([2], True),
        ([1, 2, 4], False),
        ([4, 5], False),
        ([21], True),
        ([13, 21], True),
        ([2, 3, 5], True),
        ([3, 3, 6], False)
])
def test_data_with_len_less_than_3(test_input, expected):
    assert check_fibonacci(test_input) == expected
