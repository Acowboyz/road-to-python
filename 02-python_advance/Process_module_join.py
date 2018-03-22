# Use this module to generate child process instead of using fork().
# this will fit all the windows and unix system
from multiprocessing import Process
import time
import random

Process()

def test():
    #for i in range(random.randint(1,5)):
    for i in range(1,5):
        print("test %d"%i)
        time.sleep(1)

p = Process(target = test)
# make this process to excute test function
p.start()

# Main process will wait for all child process. 
# p.join(timeout)
p.join()

print("main")
