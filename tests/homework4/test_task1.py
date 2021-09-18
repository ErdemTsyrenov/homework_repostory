import pytest

from tempfile import NamedTemporaryFile

from homework4.task1 import read_magic_number


@pytest.mark.parametrize('file_content, expected', [('1233135432\n', False)])
def test_one_line_file_with_big_integer_only(file_content, expected):
    with NamedTemporaryFile(mode='w+t') as temp:
        temp.write(file_content)
        temp.seek(0)
        assert read_magic_number(temp.name) == expected


@pytest.mark.parametrize('file_content', [('c12d3a\n')])
def test_one_line_file_with_letters(file_content):
    with NamedTemporaryFile(mode='w+t') as temp:
        temp.write(file_content)
        temp.seek(0)
        read_magic_number(temp.name)


@pytest.mark.parametrize('file_content, expected', [('1\n', True)])
def test_one_line_file_with_right_integer(file_content, expected):
    with NamedTemporaryFile(mode='w+t') as temp:
        temp.write(file_content)
        temp.seek(0)
        assert read_magic_number(temp.name) == expected


@pytest.mark.parametrize('file_content, expected', [('1\n232\n', True)])
def test_one_line_file_with_right_integer(file_content, expected):
    with NamedTemporaryFile(mode='w+t') as temp:
        temp.write(file_content)
        temp.seek(0)
        assert read_magic_number(temp.name) == expected


def test_non_exist_file():
    read_magic_number('example.txt')
