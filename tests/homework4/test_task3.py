from homework4.task3 import my_precious_logger


def test_error(capsys):
    my_precious_logger('error: one two three')
    captured = capsys.readouterr()
    assert captured.out == ''
    assert captured.err == 'error: one two three\n'


def test_non_error(capsys):
    my_precious_logger('one two three')
    captured = capsys.readouterr()
    assert captured.out == 'one two three\n'
    assert captured.err == ''
