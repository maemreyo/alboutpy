def interpolation_search(_list, item):
    idx0 = 0
    idxn = len(_list) - 1
    found = False

    while idx0 <= idxn and _list[idx0] <= item <= _list[idxn]:
        # Find the mid-point
        mid = idx0 + int((float(idxn - idx0) / (_list[idxn] - _list[idx0])) * (item - list[idx0]))
        # Compare the value at mid-point with search value
        if _list[mid] == item:
            found = True
            return found

        if _list[mid] < item:
            idx0 = mid + 1

    return found
