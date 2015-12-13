class BinarySearchTree:
    """
    Binary Search Tree relies on the property that keys that are less than the
     parent are found in the left subtree, and keys that are greater than the
     parent are found in the right subtree.
    Binary Search tree has many applications including HashMap when some payload
     object is stored along the value and Children keep back-reference to their
     parent. That ensures finding a value in the Tree in a very short time,
     greatly reducing computational complexity compared to that of a list or heap.
    This is an implementation of a very basic Binary Search Tree. TODO:
     - add parent reference
     - add get() method
     - add delete() method
    """

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

    def find(self, val):
        if self.root:
            return self.root.find(val)
        else:
            return False

    def delete(self, val):
        if self.root:
            return self.root.delete(val)
        else:
            return False


class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.value == val:
            return False
        elif self.value > val:
            if self.left:
                return self.left.insert(val)
            else:
                self.left = Node(val)
                return True
        else:
            if self.right:
                return self.right.insert(val)
            else:
                self.right = Node(val)
                return True

    def find(self, val):
        if self.value == val:
            return True
        elif self.value > val:
            if self.left:
                return self.left.find(val)
            else:
                return False
        elif self.value < val:
            if self.right:
                return self.right.find(val)
            else:
                return False

    def is_leaf(self):
        return not (self.right or self.left)
