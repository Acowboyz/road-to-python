i = 1
while i <= 9:
    j = 1
    while j <= i:
        # end = " " will place a space after the displayed string instead of a newline
        # %2d will specify the display length
        print("%d*%d=%-2d" % (j, i, i*j), end=" ")
        j += 1
    # print the newline
    print("")
    i += 1
