from threading import Thread, Lock
import threading
import time

g_num = 0

def work1():
    print("thread name is %s"%threading.current_thread().name)
    global g_num
    mutex.acquire(g_num)
    for i in range(1000000):
        g_num += 1
    mutex.release()
    
    print("work1, g_num = %d"%g_num)


    
def work2():
    print("thread name is %s"%threading.current_thread().name)
    global g_num
    mutex.acquire(g_num)
    for i in range(1000000):
        g_num += 1
    mutex.release()
    
    print("work2, g_num = %d"%g_num)

# create the mutex lock
mutex = Lock()


p1 = Thread(target = work1)
p1.start()

p2 = Thread(target = work2)
p2.start()
