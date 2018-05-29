class Game(object):

    # class attribute
    num = 0
    # instance method
    def __init__(self):
        # instance attribute
        self.name = "mario"
        # self.num = 0

   # def game_item(self):
   #     print("!!!!!")

    def add_num(self):
        self.num = 100
    # class method
    @classmethod
    def add_num(cls):
        cls.num = 100

    # static method 
    @staticmethod
    def print_menu():
        print("1. start game")
        print("2. end game")
        print(Game.num)

game = Game()

#class method can use class or object to call.
#Game.add_num()
game.add_num()

print(Game.num)

#Game.print_menu()
game.print_menu()

print(dir(Game))
