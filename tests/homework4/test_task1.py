from tempfile import NamedTemporaryFile

from homework4.task1 import read_magic_number


def test_one_line_file_with_big_integer_only():
    with NamedTemporaryFile(mode='w+t') as temp:
        temp.write('123\n')
        temp.seek(0)
        try:
            assert read_magic_number(temp.name) is False
        except ValueError:
            pass


def test_one_line_file_with_letters():
    with NamedTemporaryFile(mode='w+t') as temp:
        temp.write('123a\n')
        temp.seek(0)
        try:
            read_magic_number(temp.name)
        except ValueError:
            pass


def test_one_line_file_with_right_integer():
    with NamedTemporaryFile(mode='w+t') as temp:
        temp.write('1\n')
        temp.seek(0)
        try:
            assert read_magic_number(temp.name) is True
        except ValueError:
            pass


def test_two_line_file_with_right_integer():
    with NamedTemporaryFile(mode='w+t') as temp:
        temp.write('1\n232\n')
        temp.seek(0)
        try:
            assert read_magic_number(temp.name) is True
        except ValueError:
            pass
