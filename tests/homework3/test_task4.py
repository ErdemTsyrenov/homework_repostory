import pytest

from homework3.task4 import is_armstrong


@pytest.mark.parametrize('test_input, answer', [(0, True)])
def test_zero(test_input, answer):
    assert is_armstrong(test_input) == answer


@pytest.mark.parametrize('test_input, answer', [(1, True)])
def test_one(test_input, answer):
    assert is_armstrong(test_input) == answer


@pytest.mark.parametrize('test_input, answer', [
    (8208, True),
    (153, True)
])
def test_ordinary_right(test_input, answer):
    assert is_armstrong(test_input) == answer


@pytest.mark.parametrize('test_input, answer', [
    (2048, False),
    (10, False)
])
def test_ordinary_wrong(test_input, answer):
    assert is_armstrong(test_input) == answer
