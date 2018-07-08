def binary_search(blist, item):
    n = len(blist)

    if n > 0:
        mid = n // 2

        if blist[mid] == item:
            return True
        elif item < blist[mid]:
            return binary_search(blist[:mid], item)
        else:
            return binary_search(blist[mid+1:], item)

    return False


def binary_search_no_recur(blist, item):
    n = len(blist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if blist[mid] == item:
            return True
        elif item < blist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    else:
        return False



if __name__ == "__main__":
    l = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(l, 17))
    print(binary_search(l, 43))
    print(binary_search_no_recur(l, 17))
