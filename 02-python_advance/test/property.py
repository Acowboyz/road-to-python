class Money(object):
    def __init__(self):
        self.money = 0

    def getMoney(self):
        print("----get----")
        return self.__money

    def setMoney(self, value):
        print("----set----")
        if isinstance(value, int):
            self.__money = value
        else:
            print("error: not a integer")

    money = property(getMoney, setMoney)

m = Money()

print(m.money)

m.money = 200

print(m.money)
