from homework1.task4 import check_sum_of_four


def brute_force(a, b, c, d):
    ans = 0
    for a_i in a:
        for b_i in b:
            for c_i in c:
                for d_i in d:
                    if a_i + b_i + c_i + d_i == 0:
                        ans += 1
    return ans


def test():
    assert check_sum_of_four([1, -2], [1, 2], [2, -1], [-1, -2]) == \
           brute_force([1, -2], [1, 2], [2, -1], [-1, -2])
    assert check_sum_of_four([1, 1], [1, 1], [1, 1], [1, 1]) == \
           brute_force([1, 1], [1, 1], [1, 1], [1, 1])
    assert check_sum_of_four([1, 1, -1], [1, 1, -1],
                             [1, 1, -1], [1, 1, -1]) == \
           brute_force([1, 1, -1], [1, 1, -1], [1, 1, -1], [1, 1, -1])
