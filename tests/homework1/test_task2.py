from homework1.task2 import check_fibonacci


def test_long_data():
    assert check_fibonacci([1, 1, 2, 3, 5, 8, 13])
    assert not check_fibonacci([1, 2, 3, 4, 5])
    assert check_fibonacci([3, 5, 8, 13, 21])
    assert check_fibonacci([1, 2, 3, 5])

def test_short_data():
    assert not check_fibonacci([])
    assert not check_fibonacci([9])
    assert check_fibonacci([1,2])
    assert check_fibonacci([0])
    assert check_fibonacci([1,1])
    assert check_fibonacci([1,1,2])
    assert check_fibonacci([1])
    assert check_fibonacci([2])
    assert not check_fibonacci([1,2,4])
    assert not check_fibonacci([4,5])
    assert check_fibonacci([21])
    assert check_fibonacci([13,21])
    assert check_fibonacci([2,3,5])
    assert not check_fibonacci([3,3,6])
