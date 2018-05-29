class Cat:

    # method
    def __init__(self, new_name = "init", new_age = 0):
        self.name = new_name
        self.age = new_age

    def __str__(self):
        return "%s's age is %d" %(self.name, self.age)

    def eat(self):
        print("eat fish")
    
    def drink(self):
        print("drink water")    

    def intro(self):
        print("%s's age is %d" %(self.name, self.age))


# init the object by class
tom = Cat("Tom", 20)
may = Cat("May", 25)
jack = Cat()
# Add the attribute
# tom.name = "Tom"
# tom.age  = 20

# may.name = "May"
# may.age  = 25

# Get the attribute
tom.intro()
may.intro()
jack.intro()

# print __str__
print(may)
