class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Duck:

    def fly(self):
        print("Duck can't fly")

    def swim(self):
        print("Duck can swim")


# common interface
def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Duck()

# passing the object
flying_test(blu)
flying_test(peggy)