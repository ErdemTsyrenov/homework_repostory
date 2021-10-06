import os

import pytest

from homework1.task3 import find_maximum_and_minimum


@pytest.fixture()
def chdir():
    cwd = os.getcwd()
    print(cwd)
    os.chdir('tests/homework1')
    yield
    os.chdir(cwd)


@pytest.mark.parametrize('test_input, expected',
                         [('test_task3_files/test1.txt', (8, 1))]
                         )
def test_ascending_numbers(chdir, test_input, expected):
    assert find_maximum_and_minimum(test_input) == expected


@pytest.mark.parametrize('test_input, expected',
                         [('test_task3_files/test2.txt', (8, 1))]
                         )
def test_descending_number(chdir, test_input, expected):
    assert find_maximum_and_minimum(test_input) == expected


@pytest.mark.parametrize('test_input, expected',
                         [('test_task3_files/test3.txt', (55, -8))]
                         )
def test_with_negative_numbers(chdir, test_input, expected):
    assert find_maximum_and_minimum(test_input) == expected


@pytest.mark.parametrize('test_input, expected',
                         [('test_task3_files/test4.txt', (4, 4))]
                         )
def test_equal_numbers(chdir, test_input, expected):
    assert find_maximum_and_minimum(test_input) == expected
