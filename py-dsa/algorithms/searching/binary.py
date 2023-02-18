def binary_search(_list, item):
    first = 0
    last = len(_list) - 1
    found = False

    while first <= last and not found:
        midpo