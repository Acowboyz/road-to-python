def w1(func):
    def inner():
        print("validation")
        if False:
            func()
        else:
            print("no authorization")
    return inner


# f1 = w1(f1)
# f1()
# decorator @w1 = w1(f1)
@w1
def f1():
    print("f1")

# f1 = w1(f1)
f1()
