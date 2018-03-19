def getNums(num):
    if num > 1:
        return num * getNums(num-1)
    else:
        return num

num = int(input("please input a number:"))

print(getNums(num))
