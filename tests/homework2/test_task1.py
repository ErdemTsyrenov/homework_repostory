import os

import pytest

from homework2.task1 import get_longest_diverse_words


@pytest.fixture()
def chdir():
    cwd = os.getcwd()
    print(cwd)
    os.chdir('tests/homework2')
    yield
    os.chdir(cwd)


def test_get_longest_diverse_words(chdir):
    get_longest_diverse_words('data.txt')
