import queue
class Node:
    # The height of a leaf is considered 1.
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    # A function to perform left rotation upon insertion
    def left_rotate(self,z):
        y = z.right
        temp = y.left
        # Performing the rotation
        y.left = z
        z.right = temp
        # Recalculating the heights of the changed nodes
        z.height = 1 + max(self.height(z.left),self.height(z.right))
        y.height = 1 + max(self.height(y.left),self.height(y.right))
        # Returning the new root
        return y

    # A function to perform right rotation upon insertion
    def right_rotate(self,z):
        y = z.left
        temp = y.right
        # Performing the rotation
        y.right = z
        z.left = temp
        # Recalculating the heights of the changed nodes
        z.height = 1 + max(self.height(z.left),self.height(z.right))
        y.height = 1 + max(self.height(y.left),self.height(y.right))
        return y

    # A function to calculate the balance factor of a particular node
    def find_balance_factor(self,node):
        return self.height(node.left) - self.height(node.right)

    # Performs standard BST operation and then balances the tree
    def insert(self,root,data):
        # BST insertion
        if root is None:
            return Node(data)
        else:
            if data > root.data:
                root.right = self.insert(root.right, data)
            else:
                root.left = self.insert(root.left, data)
        # Updating the height of the node
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        # Finding the balance factor of the node
        bf = self.find_balance_factor(root)
        # Checking if balancing is needed
        # Left-Left Case
        if bf > 1 and data < root.left.data:
            return self.right_rotate(root)
        # Left-Right Case
        elif bf > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right-Right Case
        if bf < -1 and data > root.right.data:
            return self.left_rotate(root)
        # Right-Left Case
        elif bf < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    # A function to find the inorder successor
    def find_inorder_successor(self, root):
        x = root.right
        while x.left is not None:
            x = x.left
        return x

    # A function to delete a node
    def delete_node(self, root, value):
        if root is None:
            return root
        if value > root.data:
            root.right = self.delete_node(root.right, value)
        elif value < root.data:
            root.left = self.delete_node(root.left, value)
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
        if root is None:
            return root
        root.height = 1 + max(self.height(root.right), self.height(root.left))
        bf = self.find_balance_factor(root)
        # Checking if there is any imbalance
        # Left-Left Case
        if bf > 1 and self.find_balance_factor(root.left) >= 0:
            return self.right_rotate(root)
        # Left-Right Case
        elif bf > 1 and self.find_balance_factor(root.left) <= 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right-Right Case
        elif bf < -1 and self.find_balance_factor(root.right) < 0:
            return self.left_rotate(root)
        # Right-Left Case
        elif bf < -1 and self.find_balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def search(self, root, value):
        if root is None:
            return False
        if root.data == value:
            return True
        elif value > root.data:
            self.search(value, root.right)
        else:
            self.search(value, root.left)

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


