def insertion_sort(_list):
    for i in range(1, len(_list)):
        j = i - 1
        element_next = _list[i]

        while (_list[j] > element_next) and (j >= 0):
            _list[j + 1] = _list[j]
            j = j - 1
        _list[j + 1] = element_next
    return _list
