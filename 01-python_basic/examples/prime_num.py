def find_the_prime_number(start, end):
    l = []
    for n in range(start, end + 1):
        threshold_num = int(n ** 0.5)
        if threshold_num >= 2:
            for t in range(2, threshold_num + 1):
                if n % t == 0:
                    break
            else:
                l.append(n)
        else:
            l.append(n)

    return l

print(find_the_prime_number(100, 200))
