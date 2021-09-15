import pytest

from homework1.task4 import check_sum_of_four


def brute_force(a: int, b: int, c: int, d: int):
    ans = 0
    for a_i in a:
        for b_i in b:
            for c_i in c:
                for d_i in d:
                    if a_i + b_i + c_i + d_i == 0:
                        ans += 1
    return ans


@pytest.mark.parametrize('test_input, expected', [
    ([[1, -2], [1, 2], [2, -1], [-1, -2]],
     brute_force([1, -2], [1, 2], [2, -1], [-1, -2]))
])
def test_data_with_len_2(test_input, expected):
    assert check_sum_of_four(*test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([[1, 1], [1, 1], [1, 1], [1, 1]],
     brute_force([1, 1], [1, 1], [1, 1], [1, 1]))
])
def test_data_with_equal_numbers(test_input, expected):
    assert check_sum_of_four(*test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([[1, 1, -1], [1, 1, -1], [1, 1, -1], [1, 1, -1]],
     brute_force([1, 1, -1], [1, 1, -1], [1, 1, -1], [1, 1, -1]))
])
def test_data_with_len_3(test_input, expected):
    assert check_sum_of_four(*test_input) == expected
