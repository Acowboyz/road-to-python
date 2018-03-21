import types

class Person(object):
    def __init__(self, newname):
        self.name = newname

def run(self):
    print("run!!!")
    print("self.name = %s"%self.name)

@staticmethod
def staticme():
    print("static method")

@classmethod
def classme(cls):
    print("class method")

p1 = Person("felix")

p1.run = types.MethodType(run, p1)

Person.staticme = staticme

Person.classme = classme

p1.classme()

p1.staticme()

p1.run()
