def linear_search(_list, item):
    index = 0
    found = False

    while index < len(_list) and found is False:
        if _list[index] == item:
            found = True
        else:
            index += 1

    return found
