from homework1.task3 import find_maximum_and_minimum


def test_all():
    assert find_maximum_and_minimum('tests/homework1/test_task3_files/test1.txt') == (8, 1)
    assert find_maximum_and_minimum('tests/homework1/test_task3_files/test2.txt') == (8, 1)
    assert find_maximum_and_minimum('tests/homework1/test_task3_files/test3.txt') == (55, -8)
    assert find_maximum_and_minimum('tests/homework1/test_task3_files/test4.txt') == (4, 4)
    