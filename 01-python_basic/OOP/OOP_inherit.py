# parent
class Animal:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def intro(self):
        self.__intro()

    def __intro(self):
        print("name:{}, age:{}".format(self.__name, self.__age))


# child of Animal
class Dog(Animal):
    def bark(self):
        print("wang wang wang !!!")


class Cat(Animal):
    pass


# child of Dog
class Husky(Dog):
    # rewrite the method of the parent
    def bark(self):
        print("woo woo woo !!!")
        # call the method of the parent which is rewritten
        super().bark()

    def intro(self):
        print("I am Husky.")
        super().intro()


tom = Husky("tom", "2")
tom.bark()
tom.intro()

