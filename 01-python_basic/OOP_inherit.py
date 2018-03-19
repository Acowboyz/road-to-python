# parent
class Animal:
    def eat(self):
        print("eat")
    def drink(self):
        print("drink")

# child of Animal
class Dog(Animal):
    def bark(self):
        print("wang wang wang !!!")

class Cat(Animal):
    pass

# child of Dog
class Husky(Dog):
    # rewirte the method of the parent
    def bark(self):
        print("woo woo woo !!!")
        # call the method of the parent which is rewritten
        super().bark()

tom = Husky()
tom.bark()

