def func_arg(arg):
    def func(functionname):
        def func_in(*args, **kwargs):
            print("log arg=%s"%arg)
            functionname(*args,**kwargs) 
        return func_in
    return func

# 1. excute the function func_arg("haha"), return the ref of func
# 2. @fune
# 3. use @func to  decorate test
@func_arg("haha")
def test():
    print("test")

test()
