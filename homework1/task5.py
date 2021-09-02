from typing import List
from heapq import *

def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    sums = []
    current_sum = 0    
    heappush(sums, (0, -1))
    max_sum = -1e9
    for  i, elem in enumerate(nums):
        current_sum += elem
        while sums[0][1] < i - k:
            heappop(sums)
        max_sum = max(max_sum, current_sum - sums[0][0])
        heappush(sums, (current_sum, i))
    return max_sum
