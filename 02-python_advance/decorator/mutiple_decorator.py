def makeBold(fn):
    def wrapped():
        print("---1---")
        return "<b>" + fn() + "</b>"
    return wrapped

def makeItalic(fn):
    def wrapped():
        print("---2---")
        return "<i>" + fn() + "</i>"
    return wrapped
# The function will be decorated when python iterpretor runs to this code.
@makeBold # 2. helloworld = makeBold(helloworld)
@makeItalic # 1. helloworld = makeItalic(helloworld)
def helloworld():
    print("---3---")
    return "hello world-3"


print(helloworld())
