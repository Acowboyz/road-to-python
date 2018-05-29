class Dog(object):

    # private attribute
    __instance = None
    __init_flag = False

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else :
            # return previous reference
            return cls.__instance

    def __init__(self, name):
        if Dog.__init_flag is False:
            Dog.__init_flag = True
            self.name = name
        else:
            pass


a = Dog("wang")
b = Dog("black")

print(id(a))
print(id(b))

print(a.name)
print(b.name)
