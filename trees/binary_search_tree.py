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
    Binary Search Tree is also fairly easy to implement.
    """

    def __init__(self):
        self.root = None

    def __(self, instance, owner):
        return self.root

    def recursive_search(self, node, key):
        """
        Basic recursive search. Search can start at any node. Base case: the
         matching key is found, the search is successful and the Node is returned.
         This search takes advantage of the Binary Search Tree structure, it "knows"
         in what direction it has to "dig".
        """
        if node is None or key == node.key:
            return node
        elif key < node.key:
            return self.recursive_search(node.left, key)
        else:
            return self.recursive_search(node.right, key)

    def iterative_search(self, node, key):
        """
        Search using simple iteration.
        """
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
        """
        Insertion begins as a search would begin. We examine the root and
         recursively insert the new node to the left subtree if its key is less
         than that of the root, or the right subtree if its key is greater than
         the root. This implementation raises an error on duplicate keys, but we
         could as well replace the value (see replace_node()).
        This method can also be done recursively similar to recursive_search()
         given that a reference to the current node will be passed along.
        """
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
        """
        Replaces selected node and updates references to itself in the parent.
        """
        if node == self.root:
            self.root = new_node
            return True
        parent = node.parent
        if parent.left and parent.left == node:
            parent.left = new_node
        elif parent.right and parent.right == node:
            parent.right = new_node
        else:
            # Orphaned node?
            raise KeyError("Incorrect parent-children relation")

    def remove_node(self, node):
        """
        Deletion is a little complex. There are 3 possible cases:
         - Node has two children. Find its in-order successor (left-most node in
          its right sub-tree), let's call it R. We copy R's key and value to
          the node, and remove R from its right sub-tree.
         - Node has one child. The node is deleted and is replaces with its child
         - Node is a leaf and is simply removed
        """
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
        """
        Finds a node and removes it using the algorithm above.
        """
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
In-order Tree Traversals with callback functions. First parameter is a starting
 node. Pre-order or post-order traversals are done in similar way (see
 parse_tree_traversal.py), but are not likely to be useful for Binary Search Tree.

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
