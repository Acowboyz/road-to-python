def selection_sort(select_list):
    n = len(select_list)
    for j in range(0, n-1):
        min_index = j
        for i in range(j+1, n):
            if select_list[min_index] > select_list[i]:
                min_index = i
        select_list[j], select_list[min_index] = select_list[min_index], select_list[j]

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    selection_sort(li)
    print(li)
