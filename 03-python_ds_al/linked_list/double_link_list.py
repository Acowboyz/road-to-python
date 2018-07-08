class Node(object):
    def __init__(self, item):
        self.element = item
        self.next = None
        self.prev = None

class DoubleLinkList(object):
    """"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cursor = self.__head
        # count the number
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.next

        return count

    def travel(self):
        cursor = self.__head
        while cursor is not None:
            print(cursor.element, end=" ")
            cursor = cursor.next
        print("")


    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cursor = self.__head
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = node
            node.prev = cursor

    def insert(self, pos, item):
        """
        :param pos: pos is started from 0
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cursor = self.__head
            count = 0
            while count < pos:
                count += 1
                cursor = cursor.next

            # cursor is point to pos
            node = Node(item)
            node.next = cursor
            node.prev = cursor.prev
            cursor.prev.next = node
            cursor.prev = node

    def remove(self, item):
        cursor = self.__head
        while cursor != None:
            if cursor.element == item:
                # first node
                if cursor == self.__head:
                    self.__head = cursor.next
                    if cursor.next:
                        # if link list has only one node
                        cursor.next.prev = None
                else:
                    cursor.prev.next = cursor.next
                    if cursor.next:
                        cursor.next.prev = cursor.prev
                break
            else:
                cursor = cursor.next

    def search(self, item):
        cursor = self.__head

        while cursor != None:
            if cursor.element == item:
                return True
            else:
                cursor = cursor.next
        return False

if __name__ == "__main__":
    double_list = DoubleLinkList()
    print(double_list.is_empty())
    print(double_list.length())
    double_list.travel()
    double_list.append(1)
    print(double_list.is_empty())
    print(double_list.length())

    double_list.append(2)
    double_list.add(8)
    double_list.append(3)
    double_list.insert(-1,10)
    double_list.insert(10,9)
    double_list.insert(2,7)
    double_list.travel()
    print(double_list.search(10))
    double_list.remove(10)
    double_list.travel()
    double_list.remove(9)
    double_list.travel()
