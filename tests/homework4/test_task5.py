import pytest

from homework4.task5 import fizzbuzz


@pytest.mark.parametrize('test_input, expected',
                         [(4, ['1', '2', 'fizz', '4'])])
def test_first_four_nums(test_input, expected):
    assert list(fizzbuzz(test_input)) == expected


@pytest.mark.parametrize('test_input, expected',
                         [(6, ['1', '2', 'fizz', '4', 'buzz', 'fizz'])])
def test_first_six_nums(test_input, expected):
    assert list(fizzbuzz(test_input)) == expected


@pytest.mark.parametrize('test_input, expected',
                         [(16, ['1', '2', 'fizz', '4', 'buzz', 'fizz',
                                '7', '8', 'fizz', 'buzz', '11', 'fizz',
                                '13', '14', 'fizzbuzz', '16'])])
def test_first_sixteen_nums(test_input, expected):
    assert list(fizzbuzz(test_input)) == expected
