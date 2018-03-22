# Use this module to generate child process instead of using fork().
# this will fit all the windows and unix system
from multiprocessing import Process
import time

Process()

def test():
    while True:
        print("test")
        time.sleep(1)

p = Process(target = test)
# make this process to excute test function
p. start() 

# Main process will wait for all child process. 
while True:
    print("main")
    time.sleep(1)
