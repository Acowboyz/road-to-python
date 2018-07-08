class PowTwo(object):
    """class to implement an iterator of powers of two"""

    def __init__(self, max = 0):
        self.max = max
        self.n = 0

    # The __iter__() method returns the iterator object itself. If required, some initialization can be performed.
    def __iter__(self):
        self.n = 0
        return self

    # The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


pt = PowTwo(4)
i = iter(pt)
print(pt.__next__())
print(pt.__next__())
print(pt.__next__())
print(pt.__next__())
print(pt.__next__())
print(pt.__next__())

# for pt_i in pt:
#     print(pt_i)

