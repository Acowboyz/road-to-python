class Tool(object):

    # class attribute
    num = 0

    # method
    def __init__ (self, new_name):
        # instance attribute
        self.name = new_name
        Tool.num +=1

tool1 = Tool("gun")
tool2 = Tool("house")

print(Tool.num)
