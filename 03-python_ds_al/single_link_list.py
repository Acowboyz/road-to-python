class Node(object):
    """"""
    def __init__(self, element):
       self.element = element
       self.next = None

#node = Node(10)

class SingleLinkList(object):
    """"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cursor = self.__head
        # count the number
        count = 0
        while cursor != None:
            count += 1
            cursor = cursor.next

        return count

    def travel(self):
        cursor = self.__head
        while cursor != None:
            print(cursor.element, end=" ")
            cursor = cursor.next
        print("")


    def add(self, item):
        node = Node(item)
        node.next = self.__head
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

    def insert(self, pos, item):
        """
        :param pos: pos is started from 0
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            prior = self.__head
            count = 0
            while count < (pos-1):
                prior = prior.next
                count += 1

            # prior is point to (pos-1)
            node = Node(item)
            node.next = prior.next
            prior.next = node


    def remove(self, item):
        prior = None
        cursor = self.__head
        while cursor != None:
            if cursor.element == item:
                # first node
                if cursor == self.__head:
                    self.__head = cursor.next
                else:
                    prior.next = cursor.next
                break
            else:
                prior = cursor
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
    #node = Node(100)
    single_list = SingleLinkList()
    print(single_list.is_empty())
    print(single_list.length())
    single_list.travel()
    single_list.append(1)
    print(single_list.is_empty())
    print(single_list.length())

    single_list.append(2)
    single_list.add(8)
    single_list.append(3)
    single_list.insert(-1,10)
    single_list.insert(10,9)
    single_list.insert(2,7)
    single_list.travel()
    print(single_list.search(10))
    single_list.remove(10)
    single_list.travel()
    single_list.remove(9)
    single_list.travel()

