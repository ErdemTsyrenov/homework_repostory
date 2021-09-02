from typing import List
from collections import defaultdict


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    sum_ab = defaultdict(int)
    for a_i in a:
        for b_i in b:
            sum_ab[a_i + b_i] += 1
    ans = 0
    for c_i in c:
        for d_i in d:
            ans += sum_ab[-c_i - d_i]
    return ans

