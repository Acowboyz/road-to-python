import sys

class test:
    def __del__(self):
        print("this class died")

T = test()

# This process will create another reference to count
print(sys.getrefcount(T))

del T
