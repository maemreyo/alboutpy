def binary_search(_list, item):
    first = 0
    last = len(_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found
