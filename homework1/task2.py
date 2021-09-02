from typing import Sequence

def build_fibonacci(x):
    fib_seq = [0, 1]
    current = 0
    while current < x:
        current = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(current)
    return fib_seq


def find_start(fib_seq, data):
    ans = -1
    for i in range(len(fib_seq)):
        if fib_seq[i] == data[0]:
            ans = i
            break
    if len(data) > 1 and data[0] == 1 and data[1] == 2:
        ans += 1
    return ans


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) == 0:
        return False
    fib_seq = build_fibonacci(data[-1])
    start_pos = find_start(fib_seq, data)
    if start_pos == -1:
        return False
        
    for i in range(len(data)):
        if data[i] != fib_seq[start_pos + i]:
            return False
    return True
