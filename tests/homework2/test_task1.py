import os
from homework2.task1 import get_longest_diverse_words


def test_get_longest_diverse_words():
    os.chdir('tests/homework2')
    get_longest_diverse_words('data.txt')
