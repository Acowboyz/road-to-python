def shell_sort(shell_list):
    n = len(shell_list)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if shell_list[i] < shell_list[i-gap]:
                    shell_list[i], shell_list[i-gap] = shell_list[i-gap], shell_list[i]
                    i -= gap
                else:
                    break
        gap //= 2


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)
