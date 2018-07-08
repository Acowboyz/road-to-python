def quick_sort(q_list, start, end):

    if start >= end:
        return

    mid_value = q_list[start]
    low = start
    high = end

    while low < high:
        while low < high and q_list[high] >= mid_value:
            high -= 1
        else:
            q_list[low] = q_list[high]

        while low < high and q_list[low] < mid_value:
            low += 1
        else:
            q_list[high] = q_list[low]

    # low == high
    q_list[low] = mid_value

    # sort the low part
    quick_sort(q_list, start, low-1)

    # sort the high part
    quick_sort(q_list, low+1, end)

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)
