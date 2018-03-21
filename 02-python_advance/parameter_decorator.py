def func(functionname):
    def func_in(*args, **kwargs):
        functionname(*args,**kwargs) 

    return func_in

@func
def test(a, b, c):
    print("%d, %d, %d"%(a, b, c))

test(11,22,33)
