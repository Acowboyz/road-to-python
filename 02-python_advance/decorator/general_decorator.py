def func(functionname):
    def func_in(*args, **kwargs):
        ret = functionname(*args, **kwargs) 
        return ret

    return func_in

@func
def test1():
    print("test1")

@func
def test2():
    print("test2")
    return "haha"

@func
def test3(a):
    print("test3 = %d"%a)

print(test1())

print(test2())

print(test3(1))
