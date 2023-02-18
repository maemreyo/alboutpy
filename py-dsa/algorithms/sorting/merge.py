def merge_sort(_list):
    if len(_list) > 1:
        mid = len(_list) // 2
        left = _list[:mid]
        right = _list[mid:]

        merge_sort(left)
        merge_sort(right)

        a = 0
        b = 0
        c = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                _list[c] = left[a]
                a += 1
            else:
                _list[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            _list[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            _list[c] = right[b]
            b += 1
            c += 1
    return _list
