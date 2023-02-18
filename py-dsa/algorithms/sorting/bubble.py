def bubble_sort(_list):
    last_element_index = len(_list) - 1

    for passIndex in range(last_element_index, 0, -1):
        for index in range(passIndex):
            if _list[index] > _list[index + 1]:
                _list[index], _list[index + 1] = _list[index + 1], _list[index]

    return _list
