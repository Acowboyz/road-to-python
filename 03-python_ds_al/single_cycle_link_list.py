class Node(object):
    """"""

    def __init__(self, element):
        self.element = element
        self.next = None


class SingleCycleLinkList(object):
    """"""

    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        if self.is_empty():
            return 0

        cursor = self.__head
        # count the number
        count = 1
        while cursor.next != self.__head:
            count += 1
            cursor = cursor.next

        return count

    def travel(self):
        if self.is_empty():
            return

        cursor = self.__head
        while cursor.next != self.__head:
            print(cursor.element, end=" ")
            cursor = cursor.next
        # print the end node
        print(cursor.element)

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cursor = self.__head

            # find the end node
            while cursor.next != self.__head:
                cursor = cursor.next

            node.next = self.__head
            self.__head = node
            cursor.next = self.__head

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cursor = self.__head

            while cursor.next != self.__head:
                cursor = cursor.next

            node.next = self.__head
            cursor.next = node

    def insert(self, pos, item):
        """
        :param pos: pos is started from 0
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            prior = self.__head
            count = 0
            while count < (pos - 1):
                prior = prior.next
                count += 1

            # prior is point to (pos-1)
            node = Node(item)
            node.next = prior.next
            prior.next = node

    def remove(self, item):
        if self.is_empty():
            return

        prior = None
        cursor = self.__head
        while cursor.next != self.__head:
            if cursor.element == item:
                # first node
                if cursor == self.__head:

                    # find the end node to point to the first node
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    else:
                        self.__head = cursor.next
                        rear.next =self.__head

                # mid node
                else:
                    prior.next = cursor.next
                return
            else:
                prior = cursor
                cursor = cursor.next
        # end node
        else:
            if cursor.element == item:
                if cursor == self.__head:
                    # link list has only one node
                    self.__head = None
                else:
                    prior.next = cursor.next

    def search(self, item):
        if self.is_empty():
            return False

        cursor = self.__head

        while cursor != self.__head:
            if cursor.element == item:
                return True
            else:
                cursor = cursor.next
        # if end node == item
        if cursor.element == item:
            return True

        return False

if __name__ == "__main__":
    single_list = SingleCycleLinkList()
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
