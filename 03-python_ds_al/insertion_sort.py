def insertion_sort(insert_list):
    i = 1
    n = len(insert_list)
    for j in range(1, n):
        i = j
        while i > 0:
            if insert_list[i] < insert_list[i-1]:
                insert_list[i] , insert_list[i-1] = insert_list[i-1], insert_list[i]
                i -= 1
            else:
                break

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insertion_sort(li)
    print(li)

