import pytest

from homework4.task3 import my_precious_logger


@pytest.mark.parametrize('test_input, stdout_expected, stderr_expected',
                         [('error: one two three', '',
                           'error: one two three\n')])
def test_error(capsys, test_input, stdout_expected, stderr_expected):
    my_precious_logger(test_input)
    captured = capsys.readouterr()
    assert captured.out == stdout_expected
    assert captured.err == stderr_expected


@pytest.mark.parametrize('test_input, stdout_expected, stderr_expected',
                         [('one two three', 'one two three\n', '')])
def test_non_error(capsys, test_input, stdout_expected, stderr_expected):
    my_precious_logger(test_input)
    captured = capsys.readouterr()
    assert captured.out == stdout_expected
    assert captured.err == stderr_expected
