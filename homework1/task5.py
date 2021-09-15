from heapq import heappop, heappush
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    answer to this task looks like S[i]-S[j] where i-j+1 <= k and
    S[i] = sum of elements from 0 to i. Our goal is for each element
    S[i] to find such element S[j] to maximize answer or in other words
    to find minimal S[j] where j >= i-k-1. To do this we can use heap.
    Heap contains pairs (S[i], i). For each S[i] we use heap.min() and
    ans = S[i] - heap.min()[0]; If heap.min()[1] < i-k we need to pop item
    Time complexity analysys:
    for each S[i] we insert S[i] to heap and delete it once. So time
    complexity is O(n*log(n))
    """
    sums = []  # heap that contains tuples (S[i], i)
    current_sum = 0
    heappush(sums, (0, -1))
    max_sum = float('-inf')
    for i, elem in enumerate(nums):
        current_sum += elem
        while sums[0][1] < i - k:
            heappop(sums)
        max_sum = max(max_sum, current_sum - sums[0][0])
        heappush(sums, (current_sum, i))
    return max_sum
