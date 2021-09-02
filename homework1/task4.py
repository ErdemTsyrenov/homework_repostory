from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    n = 0
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                for l in range(len(d)):
                    if a[i]+b[j]+c[k]+d[l] == 0:
                        n += 1
    return n