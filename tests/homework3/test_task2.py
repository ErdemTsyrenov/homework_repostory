import time
from homework3.task2 import calculate_total


def test_time_limit():
    start = time.time()
    calculate_total()
    assert time.time() - start < 60
