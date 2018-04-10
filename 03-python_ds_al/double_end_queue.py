class DoubleEndQueue(object):

    def __init__(self):
        self.__queue = []

    def add_front(self, item):
        self.__queue.insert(0, item)

    def add_rear(self, item):
        self.__queue.append(item)

    def pop_front(self):
        return self.__queue.pop(0)

    def pop_rear(self):
        return  self.__queue.pop()

    def is_empty(self):
        return self.__queue == []

    def size(self):
        return len(self.__queue)

if __name__ == "__main__":
    q = DoubleEndQueue()
    q.add_front(1)
    q.add_front(2)
    q.add_front(3)
    q.add_front(4)
    q.add_rear(1)
    q.add_rear(2)
    q.add_rear(3)
    q.add_rear(4)
    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_rear())
    print(q.pop_rear())
    print(q.pop_rear())
    print(q.pop_rear())
