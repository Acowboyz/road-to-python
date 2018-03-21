def func(functionname):
    def func_in():
        return functionname() 

    return func_in

@func
def test():
    print("test")
    return "haha"

print(test())
