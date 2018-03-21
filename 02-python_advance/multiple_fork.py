import os
import time

ret = os.fork()

if ret == 0:
    print("1")
else:
    print("2")

# main and child process are fork.
# will generate 4 = 2^n , n=2 process
ret = os.fork()
if ret == 0:
    # child --> child
    # main  --> child
    print("11")
else:
    # child
    # main
    print("22")


