import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def levelorder(self, root):
        levelq = queue.Queue()
        if root is None:
            return
        levelq.put(root)
        while not levelq.empty():
            x = levelq.get()
            print("{0} ".format(x.data), end="")
            if x.left is not None:
                levelq.put(x.left)
            if x.right is not None:
                levelq.put(x.right)
        print("")

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print("{0} ".format(root.data), end="")
            self.inorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print("{0} ".format(root.data),end="")

    def preorder(self, root):
        if root is not None:
            print("{0} ".format(root.data), end="")
            self.preorder(root.left)
            self.preorder(root.right)

    def insert(self, root, data):
        if root is None:
            root = Node(data)
        else:
            if data > root.data:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.insert(root.right, data)
            else:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.insert(root.left, data)

    def find_inorder_successor(self, root):
        x = root.right
        while x.left is not None:
            x = x.left
        return x

    def delete_node(self, root, value):
        if root is None:
            return root
        if value > root.data:
            root.right = self.deleteNode(root.right, value)
        elif value < root.data:
            root.left = self.deleteNode(root.left, value)
        else:
            if root.right is None and root.left is None:
                root = None
                return root
            elif root.right is None and root.left is not None:
                temp = root.left
                root = None
                return temp
            elif root.right is not None and root.left is None:
                temp = root.right
                root = None
                return temp
            else:
                inheritor = self.find_inorder_successor(root)
                root.data = inheritor.data
                root.right = self.delete_node(root.right, inheritor.data)
        return root

    # Returns True if found otherwise returns False
    def search(self, root, value):
        if root is None:
            return False
        if root.data == value:
            return True
        elif value > root.data:
            self.search(value, root.right)
        else:
            self.search(value, root.left)
