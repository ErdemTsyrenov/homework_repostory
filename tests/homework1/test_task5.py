import pytest

from homework1.task5 import find_maximal_subarray_sum


@pytest.mark.parametrize('test_input, expected', [
        ([[1, 3, -1, -3, 5, 3, 6, 7], 3], 16)
])
def test_data_with_negative_nums(test_input, expected):
    assert find_maximal_subarray_sum(*test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
        ([[100, -10, 10], 3], 100)
])
def test_data_with_len_equal_k(test_input, expected):
    assert find_maximal_subarray_sum(*test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([[3, 4, 2, -200, -100, 1000], 4], 1000),
    ([[1, 2, -1, 5, -10], 2], 5)
])
def test_with_result_subarray_as_one_number(test_input, expected):
    assert find_maximal_subarray_sum(*test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([[1, 2, -1, 3, -10], 1], 3)
])
def test_with_k_equal_one(test_input, expected):
    assert find_maximal_subarray_sum(*test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([[1], 1], 1)
])
def test_with_len_equal_one(test_input, expected):
    assert find_maximal_subarray_sum(*test_input) == expected
