import pytest

from homework7.task2 import backspace_compare


@pytest.mark.parametrize('test_input, expected', [
    (["ab#c", "ad#c"], True),
    (["a##c", "#a#c"], True),
])
def test_same_length(test_input, expected):
    assert backspace_compare(*test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    (["a#c", "b"], False),
    (["d#da#c", "aac"], False),
    (["d#d#ac", "a#ac"], True),
    (["", "a#ac"], False)
])
def test_diff_length(test_input, expected):
    assert backspace_compare(*test_input) == expected
