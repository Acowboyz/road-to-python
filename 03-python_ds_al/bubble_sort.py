def bubble_sort(bubblelist):
    # O(n^2)
    n = len(bubblelist)
    for j in range(0, n-1):
        for i in range(0, n-1-j):
            if bubblelist[i] > bubblelist[i+1]:
                bubblelist[i], bubblelist[i+1] = bubblelist[i+1], bubblelist[i]


def bubble_sort_optimal(bubblelist):
    # optimal case O(n), worst case O(n^2)
    n = len(bubblelist)
    for j in range(0, n-1):
        count = 0
        for i in range(0, n-1-j):
            if bubblelist[i] > bubblelist[i+1]:
                bubblelist[i], bubblelist[i+1] = bubblelist[i+1], bubblelist[i]
                count += 1
        # can handle [1, 2, 3, 4, 5]
        if 0 == count:
            return

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)