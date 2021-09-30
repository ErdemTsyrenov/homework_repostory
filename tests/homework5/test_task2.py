import functools
from typing import Callable

import pytest

from homework5.task2 import print_result


@print_result
def custom_sum(*args):
    """Sum objects"""
    return functools.reduce(lambda x, y: x + y, args)


@pytest.mark.parametrize('func, doc_value',
                         [(custom_sum, 'Sum objects')])
def test_doc(func: Callable, doc_value: str):
    assert func.__doc__ == doc_value


@pytest.mark.parametrize('func, name_value',
                         [(custom_sum, 'custom_sum')])
def test_name(func: Callable, name_value: str):
    assert func.__name__ == name_value


@pytest.mark.parametrize('func, func_input, stdout',
                         [(custom_sum, [[1, 2, 3], [4, 5]],
                           '[1, 2, 3, 4, 5]\n')])
def test_stdout(capsys, func: Callable, func_input: str, stdout: str):
    func(*func_input)
    captured = capsys.readouterr()
    assert captured.out == stdout


@pytest.mark.parametrize('func, func_input, stdout',
                         [(custom_sum, [[1, 2, 3], [4, 5]], '')])
def test_original(capsys, func: Callable, func_input: str, stdout: str):
    func.__original_func__(*func_input)
    captured = capsys.readouterr()
    assert captured.out == stdout
