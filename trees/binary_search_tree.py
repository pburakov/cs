class BinarySearchTree:
    """
    Binary Search Tree relies on the property that keys that are less than the
     parent are found in the left subtree, and keys that are greater than the
     parent are found in the right subtree.
    Binary Search Tree is similar to Binary Heap but has many applications
     including HashMap when some payload object is stored along the value
     and Children keep back-reference to their parent. That ensures finding
     a value in the Tree in a very short time, greatly reducing number of
     comparisons for well-balanced trees.
    Binary Search Tree is also very easy to implement using recursion.
    """

    def __init__(self):
        self.root = None

    def __(self, instance, owner):
        return self.root

    def recursive_search(self, node, key):
        if node is None or key == node.key:
            return node
        elif key < node.key:
            return self.recursive_search(node.left, key)
        else:
            return self.recursive_search(node.right, key)

    def iterative_search(self, node, key):
        current_node = node
        while current_node:
            if key == current_node.key:
                return current_node
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            return True
        current_node = self.root
        while current_node:
            if key == current_node.key:
                raise KeyError("Duplicate key")
            elif key < current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(key, value, parent=current_node)
                    return True
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(key, value, parent=current_node)
                    return True

    def replace_node(self, node, new_node):
        if node == self.root:
            self.root = new_node
            return True
        parent = node.parent
        if parent.left and parent.left == node:
            parent.left = new_node
        elif parent.right and parent.right == node:
            parent.right = new_node
        else:
            raise RuntimeError("Incorrect parent-children relation")

    def remove_node(self, node):
        if node.left and node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
            node.key = successor.key
            node.value = successor.value
            self.remove_node(successor)
        elif node.left:
            self.replace_node(node, node.left)
        elif node.right:
            self.replace_node(node, node.right)
        else:
            self.replace_node(node, None)

    def delete(self, key):
        node = self.iterative_search(self.root, key)
        if node:
            self.remove_node(node)


class Node:
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


"""
Tree Traversals with callback functions, first parameter is a starting node.

Example usage:
    bst = BinarySearchTree()
    bst.insert('d', 12)
    bst.insert('b', 214)
    bst.insert('c', 1124)
    bst.insert('a', 24)

    # Prints list of sorted keys and values
    traverse_in_order(bst.root, lambda node: print(node.key, node.value))

    # Saves sorted list of keys ['a, 'b', 'c', 'd']
    sorted_keys = []
    traverse_in_order(bst.root, lambda node: sorted_keys.append(node.key))
"""


def traverse_in_order(node, function):
    if node is None:
        return None
    traverse_in_order(node.left, function)
    function(node)
    traverse_in_order(node.right, function)


def traverse_pre_order(node, function):
    if node is None:
        return None
    function(node)
    traverse_in_order(node.left, function)
    traverse_in_order(node.right, function)


def traverse_post_order(node, function):
    if node is None:
        return None
    traverse_in_order(node.left, function)
    traverse_in_order(node.right, function)
    function(node)
