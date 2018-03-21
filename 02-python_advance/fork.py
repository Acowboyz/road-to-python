import os
import time

ret = os.fork()
# mutitask process
print (ret)
if ret == 0:
    # child process
    while True:
        # process pid, parent process pid
        print("child %d %d"%(os.getpid(), os.getppid()))
        time.sleep(1)
else:
    # main process
    while True:
        # process pid
        print("parent %d"%os.getpid())
        time.sleep(1)
