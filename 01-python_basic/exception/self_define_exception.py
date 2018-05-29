class ShortInputException(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast


def main():
    try:
        s = input("please input:")
        if len(s) < 3:
        # use rasie to cause the self-defined exception
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:
        print("ShortInputException : input length is %d, length shold not be less than %d"%(result.length, result.atleast))
    else:
        print("No exception occur")


main()
