class BinaryTree:
    def __init__(self):
        """
        Binary Tree set representation class that holds a pointer to its root.
        """
        self.root = None


class Node:
    def __init__(self, key):
        """
        Node of a binary tree.

        Holds a value of any type (called a key) and pointers to left and/or right
         child.

        :param object key: Node's value (key)
        """
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


