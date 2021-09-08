from homework3.task4 import is_armstrong


def test_default():
    assert is_armstrong(153) is True
    assert is_armstrong(10) is False


def test_zero():
    assert is_armstrong(0) is True


def test_one():
    assert is_armstrong(1) is True


def test_ordinary_right():
    assert is_armstrong(8208) is True


def test_ordinary_wrong():
    assert is_armstrong(2048) is False
