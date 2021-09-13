from unittest.mock import Mock

from homework4.task2 import count_dots_on_i


def test_with_i():
    urlopen = Mock()
    urlopen.return_value = "This is the emulation of html page"
    assert count_dots_on_i("https://example.com") == 2
