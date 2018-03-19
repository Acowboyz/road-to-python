a = 100

def test1() :
    global a;
    a = 101
    print("a=%d"%a)

test1()

print(a)
