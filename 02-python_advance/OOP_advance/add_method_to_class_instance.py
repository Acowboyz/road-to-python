import types

class Person(object):
    def __init__(self, newname):
        self.name = newname


# instance method

def run(self):
    print("run!!!")
    print("self.name = %s"%self.name)


# static method

@staticmethod
def staticme():
    print("static method")

# class method

@classmethod
def classme(cls):
    print("class method")


p1 = Person("felix")

p1.run = types.MethodType(run, p1)

# p1.run = run

# Person.run = run

Person.staticme = staticme

Person.classme = classme

# delattr(Person, "classme")

p1.classme()

p1.staticme()

# p1.run(p1)
p1.run()
