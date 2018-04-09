from timeit import Timer

# list
def t1():
    l = []
    for i in range(1000):
        l = l + [i]

def t2():
    l = []
    for i in range(1000):
        l.append(i)

def t3():
    l = [i for i in range(1000)]

def t4():
    l = list(range(1000))

def t5():
    li = []
    for i in range(1000):
        li.extend([i])

def t6():
    li = []
    for i in range(1000):
        li.insert(0, i)

timer1 = Timer("t1()", "from __main__ import t1")
print("concat ",timer1.timeit(number=1000))

timer2 = Timer("t2()", "from __main__ import t2")
print("append ", timer2.timeit(number=1000))

timer3 = Timer("t3()", "from __main__ import t3")
print("comprehension ", timer3.timeit(number=1000))

timer4 = Timer("t4()", "from __main__ import t4")
print("list range ", timer4.timeit(number=1000))

timer5 = Timer("t5()", "from __main__ import t5")
print("extend ", timer5.timeit(number=1000))

timer6 = Timer("t6()", "from __main__ import t6")
print("insert ", timer6.timeit(number=1000))
