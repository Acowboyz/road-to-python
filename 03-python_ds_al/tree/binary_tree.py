class Node(object):

    def __init__(self, item):
        self.elem = item
        self.left = None
        self.right = None


class Tree(object):

    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        node = Node(item)

        if self.root is None:
            self.root = node
            return

        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            elif cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.left)
                queue.append(cur_node.right)

    def breath_traverse(self):

        if self.root is None:
            return

        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")

            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    def pre_order_traverse(self, node):

        if node is None:
            return

        print(node.elem, end=" ")

        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)

    def in_order_traverse(self, node):

        if node is None:
            return

        self.in_order_traverse(node.left)
        print(node.elem, end=" ")
        self.in_order_traverse(node.right)

    def post_order_traverse(self, node):

        if node is None:
            return

        self.post_order_traverse(node.left)
        self.post_order_traverse(node.right)
        print(node.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breath_traverse()
    print("")
    tree.pre_order_traverse(tree.root)
    print("")
    tree.in_order_traverse(tree.root)
    print("")
    tree.post_order_traverse(tree.root)
