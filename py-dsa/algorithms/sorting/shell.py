def shell_sort(_list):
    distance = len(_list) // 2

    while distance > 0:
        for i in range(distance, len(_list)):
            temp = _list[i]
            j = i

            while j >= distance and _list[j - distance] > temp:
                _list[j] = _list[j - distance]
                j = j - distance
            _list[j] = temp

        distance = distance // 2

    return _list
