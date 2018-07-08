def test(number):
    
    def test_in(number_in):
        print("in test_in function, number_in is %d"%number_in)
        return number + number_in

    return test_in


ret = test(100)
print(ret(100))
print(ret(200))

