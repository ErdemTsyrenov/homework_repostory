from typing import Iterable


def find_start_stop_idx(iterable, start, stop):
    stop_index = 0
    start_index = 0
    for i, item in enumerate(iterable):
        if item == start:
            start_index = i
        if item == stop:
            stop_index = i
    return start_index, stop_index


def get_start_stop_step(*args):
    if len(args) == 1:
        return 0, args[0], 1
    elif len(args) == 2:
        return args[0], args[1], 1
    elif len(args) == 3:
        return args[0], args[1], args[2]


def custom_range(iterable: Iterable, *args):
    start, stop, step = get_start_stop_step(*args)
    start_idx, stop_idx = find_start_stop_idx(iterable, start, stop)
    print(start_idx, stop_idx)
    indexes = list(range(start_idx, stop_idx, step))
    if step < 0:
        indexes = list(reversed(indexes))
    i = 0
    result = []
    for j, item in enumerate(iterable):
        if len(result) >= len(indexes):
            break
        if j == indexes[i]:
            result.append(item)
            i += 1
    if step < 0:
        return list(reversed(result))
    else:
        return result
