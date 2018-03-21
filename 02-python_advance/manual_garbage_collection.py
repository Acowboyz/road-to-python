import gc

class ClassA():
    def __init__(self):
        print("object born, id:%s"%str(hex(id(self))))

#In Python2 and up to Python3.2 gc.disable() is also used to avoid a bug caused by garbage collection occurring between fork and exec. The problem seems to have been fixed in Python3.3 without needing to call gc.disable().
def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        gc.collect()

#gc.disable()

f2()
