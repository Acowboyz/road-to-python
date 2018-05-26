def calc_factorial(num):
    """This is a recursive function
        to find the factorial of an integer"""
    if num > 1:
        return num * calc_factorial(num-1)
    else:
        return num

num = int(input("please input a number:"))

print("The factorial of", num, "is", calc_factorial(num))
