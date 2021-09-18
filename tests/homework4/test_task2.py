import urllib
from unittest.mock import patch

import pytest

from homework4.task2 import count_dots_on_i


@pytest.mark.parametrize('webpage_emulation, answer',
                         [("This is the emulation of html page", 3)])
def test_with_i(webpage_emulation: str, answer: int):
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.return_value = webpage_emulation
        print(urllib.request.urlopen())
        assert count_dots_on_i("https://example.com") == answer


@pytest.mark.parametrize('webpage_emulation, answer',
                         [("Text, text, text, text!", 0)])
def test_without_i(webpage_emulation: str, answer: int):
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.return_value = webpage_emulation
        print(urllib.request.urlopen())
        assert count_dots_on_i("https://example.com") == answer
