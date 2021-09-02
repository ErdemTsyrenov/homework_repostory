from homework1.task5 import find_maximal_subarray_sum


def test():
    assert find_maximal_subarray_sum([1,3,-1,-3,5,3,6,7], 3) == 16
    assert find_maximal_subarray_sum([100, -10, 10], 3) == 100
    assert find_maximal_subarray_sum([3, 4, 2, -200, -100, 1000], 4) == 1000
    assert find_maximal_subarray_sum([1,2,-1,3,-10], 1) == 3
    assert find_maximal_subarray_sum([1], 1) == 1 
    assert find_maximal_subarray_sum([1,2,-1,5,-10], 2) == 5