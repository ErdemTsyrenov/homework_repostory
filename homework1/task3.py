from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    max_val = float('-inf')
    min_val = float('inf')
    with open(file_name) as fi:
        for line in fi:
            max_val = max(int(line), max_val)
            min_val = min(int(line), min_val)
    return (max_val, min_val)
