from multiprocessing import Process
import time

g_num = 100

def test1():
    global g_num

    for i in range(3):
        g_num += 1

    print(" test1, g_num is %d"%g_num)

def test2():
    global g_num
    print(" test2, g_num is %d"%g_num)

p1 = Process(target = test1)
# make this process to excute test function
p1. start() 

time.sleep(1)

p2 = Process(target = test2)
# make this process to excute test function
p2. start() 

