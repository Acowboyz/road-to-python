class Node(object):
    """"""
    def __init__(self, element):
        self.element = element
        self.next = None


# node = Node(10)

class SingleLinkList(object):
    """ Create a single linked list"""

    def __init__(self, node=None):
        # There is no node in the linked list when initializing.
        self.__head = node

    def is_empty(self):
        # if self.__head points to the null, indicates that there is no node in the linked list.
        return self.__head is None

    def length(self):
        # cursor points to the first node instance
        cursor = self.__head
        # count the number
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.next

        return count

    def traverse(self):
        cursor = self.__head
        while cursor is not None:
            print(cursor.element, end=" ")
            cursor = cursor.next
        print("")

    def add(self, item):
        # create a new Node instance
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cursor = self.__head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = node

    def insert(self, pos, item):
        """
        :param pos: pos is started from 0
        :param item :
        """
        if pos <= 0:
            # add the item to the head
            self.add(item)
        elif pos > (self.length()-1):
            # add the item to the end
            self.append(item)
        else:
            # find the position
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
        while cursor is not None:
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

        while cursor is not None:
            if cursor.element == item:
                return True
            else:
                cursor = cursor.next
        return False


if __name__ == "__main__":
    # node = Node(100)
    single_list = SingleLinkList()
    print(single_list.is_empty())
    print(single_list.length())
    single_list.traverse()
    single_list.append(1)
    print(single_list.is_empty())
    print(single_list.length())

    single_list.append(2)
    single_list.add(8)
    single_list.append(3)
    single_list.insert(-1, 10)
    single_list.insert(10, 9)
    single_list.insert(2, 7)
    single_list.traverse()
    print(single_list.search(10))
    single_list.remove(10)
    single_list.traverse()
    single_list.remove(9)
    single_list.traverse()

