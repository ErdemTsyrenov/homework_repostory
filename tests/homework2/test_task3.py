from homework2.task3 import combinations


def test_default():
    assert combinations([1, 2], [3, 4]) == [[1, 3],
                                            [1, 4],
                                            [2, 3],
                                            [2, 4]]


def test_dif():
    assert combinations([1], [1, 2, 3]) == [[1, 1],
                                            [1, 2],
                                            [1, 3]]
