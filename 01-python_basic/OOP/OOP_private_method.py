class Dog:

    # private method
    def __send_msg(self):
        print("sending message")

    # public method
    def send_msg(self, money):
        if money> 10000:
            self.__send_msg()
        else:
            print("your money is not enough to buy the dog")


dog = Dog()
dog.send_msg(100)
dog._Dog__send_msg()
