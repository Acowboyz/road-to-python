from multiprocessing import Pool
import time
import os

def test1():
    print("processing pool pid = %d, ppid = %d"%(os.getpid(), os.getppid()))
    for i in range(3):
        print("%d"%i)
        time.sleep(1)
    return "hahaha"

def test2(args):
    print("callback func pid = %d"%os.getpid())
    print("callback func arg = %s"%args)

pool = Pool(3)

pool.apply_async(func = test1, callback= test2)


#pool.close()
#pool.join()

while True:
    time.sleep(1)
    print("main process pid = %d"%os.getpid())
