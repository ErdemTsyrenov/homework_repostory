def custom_range(iterable, start, stop=None, step=1):
    def inner_one_arg(iterable, stop=None):
        result = []
        for item in iterable:
            if item == stop:
                break
            result.append(item)
        return result

    def find_start_stop_idx(iterable, start, stop):
        stop_index = 0
        start_index = 0
        for i, item in enumerate(iterable):
            if item == start:
                start_index = i
            if item == stop:
                stop_index = i
        return start_index, stop_index

    def inner_three_args(iterable, start, stop, step):
        start_idx, stop_idx = find_start_stop_idx(iterable, start, stop)
        indexes = list(range(start_idx, stop_idx, step))
        if step < 0:
            indexes = list(reversed(indexes))
        i = 0
        result = []
        for j, item in enumerate(iterable):
            if len(indexes) <= i:
                break
            if j == indexes[i]:
                result.append(item)
                i += 1
        if step < 0:
            return list(reversed(result))
        else:
            return result

    if stop is None:
        return inner_one_arg(iterable, stop=start)
    else:
        return inner_three_args(iterable, start, stop, step)
