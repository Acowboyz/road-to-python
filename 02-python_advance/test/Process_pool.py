from multiprocessing import Pool 
import os
import random
import time

def worker(num):
    for i in range(5):
        print("pid - %d, num = %d"%(os.getpid(), num))
        time.sleep(1)

# Pool(num) : there is at most (num) processes run simutaneously in the process pool 
pool = Pool(3)

for i in range(10):
    print("%d"%i)
    # add the task in the process pool
    # 
    pool.apply_async(worker,(i,))

    # It blocks until the result is ready. Given this blocks, apply_async() is better suited for performing work in parallel.
    # pool.apply(worker,(i,))

pool.close()

# Wait for the worker processes to exit.
pool.join()

