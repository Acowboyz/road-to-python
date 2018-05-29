import sys

class Myclass(object):

    def __init__(self, name):
        self.name = name
        print("__init__")

    def __del__(self):
        print("__del__ {}".format(self.name))


M = Myclass("Felix")
M1 = M
M2 = M1

print("delete instance M")
del M

print("delete instance M1")
del M1

print("delete instance M2")
del M2
