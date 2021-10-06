import pytest

from homework2.task3 import combinations


@pytest.mark.parametrize('test_input, expected', [
    ([[1, 2], [3, 4]], [[1, 3],
                        [1, 4],
                        [2, 3],
                        [2, 4]]),
])
def test_default(test_input, expected):
    assert combinations(*test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([[1], [1, 2, 3]], [[1, 1],
                        [1, 2],
                        [1, 3]]),
])
def test_with_dif_len(test_input, expected):
    assert combinations(*test_input) == expected
