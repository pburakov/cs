"""
BST (Binary Search Tree) is a convenient Binary Tree data structure that allows
 fast value lookup. Basic operations on a complete BST take time proportional to
 a height of a tree rather that the number of its elements.

The values (or keys as named in CLRS) in a BST are stored in such a way as to
 satisfy the main BST property. For any parent node in a BST, its left child
 must hold a smaller value and its right child must hold a bigger value.

Every node in a binary tree is a root to its own subtree. Inductively, BST property
 guarantees that any value in a left subtree will be smaller than the root node
 and any value in a right subtree will be bigger.

In-order printing of nodes in a BST will produce sorted output of its values.
 Nodes in augmented BSTs can hold more properties and offer more efficient
 operations in a handful of applications.

The correctness of these algorithms is guaranteed by the BST properties. Notice
 that the update algorithms implemented here, such as `tree_insert()`, `transplant()`
 and `tree_delete()` (algorithms that cause the dynamic set represented by BST
 to change) operate on an instance of BST, while query algorithms operate on
 arbitrary nodes.

Most BST operations take O(h) time where `h` is a height of a tree. If tree is
 perfectly complete, `h` will be log(n) (see trees/balanced_tree.py). In worst
 case with all the nodes on one side, BST will resemble a linked list and take
 O(n) as it's height will be proportional to the number of elements.
"""
from trees.binary_tree import BinaryTree
from trees.binary_tree import Node as BinaryTreeNode


class BST(BinaryTree):
    """
    Represented just as a regular Binary Tree, holds a pointer to the root node.
    """
    pass


class Node(BinaryTreeNode):
    """
    Slightly augmented variant of a Binary Tree Node, that additionally holds a
     reference to its parent.
    """

    def __init__(self, key):
        super().__init__(key)
        self.parent = None


def tree_search(node, k):
    """
    Recursive search query algorithm for finding a key in BST.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node node: Node to start the search with
    :param Any k: A key (value) to search
    :return: Any: A found node or None if key `k` was not found in the tree
    """
    if node is None or node.key == k:
        return node
    elif k < node.key:
        return tree_search(node.left, k)
    elif k > node.key:
        return tree_search(node.right, k)


def iterative_tree_search(node, k):
    """
    Iterative version of BST search algorithm. It is more efficient on most
     computers due to reduced use of a memory stack.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node node: Node to start the search with
    :param Any k: A key (value) to search
    :return: Any: A found node or None if key `k` was not found in the tree
    """
    while k is not None and k != node.key:
        if k < node.key:
            node = node.left
        elif k > node.key:
            node = node.right
    return node


def tree_minimum(node):
    """
    Returns a pointer to a node holding a minimum value (key) which is a
     leftmost node as directed by BST property.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node node: Node to start the lookup
    :return: Node: Node holding minimum value
    """
    while node.left is not None:
        node = node.left
    return node


def tree_maximum(node):
    """
    Returns a pointer to a node holding a maximum value (key) which is a
     rightmost node as directed by BST property.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node node: Node to start the lookup
    :return: Node: Node holding maximum value
    """
    while node.right is not None:
        node = node.right
    return node


def tree_successor(node):
    """
    Returns element successor, or next node, determined by a sorted in-order
     tree traversal.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node node: Node to start the lookup
    :return Any: Will return successor node if it exists, None otherwise
    """
    if node.right is not None:
        # Return minimum element (leftmost node) in a right subtree --
        return tree_minimum(node.right)
    else:
        # -- or, if there is no right child, go up the tree from `node` until
        # we encounter a node that is the left child of its parent.
        p = node.parent
        while p is not None and node == p.right:
            node = p
            p = p.parent
        return p


def tree_predecessor(node):
    """
    Returns element predecessor, or previous node, determined by a sorted
     in-order tree traversal.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node node: Node to start the lookup
    :return Any: Will return predecessor node if it exists, None otherwise
    """
    if node.left is not None:
        # Return maximum element (rightmost node) in a left subtree --
        return tree_maximum(node.left)
    else:
        # -- or, if there is no left child, go up the tree from `node` until
        # we encounter a node that is the right child of its parent
        p = node.parent
        while p is not None and node == p.left:
            node = p
            p = p.parent
        return p


def tree_insert(T, z):
    """
    Inserts a new node into an appropriate position in the BST `T` in such a way,
     that the properties of BST continue to hold. This algorithm is similar to
     `tree_search()` and can also be implemented recursively.

    Complexity: O(h) where `h` is the height of a tree.
    :param BST T: BST to update
    :param Node z: New node, holding unique value (key)
    :return None: BST `T` is updated
    """
    p = None    # Pointer to a parent of a `z` node.
    q = T.root  # Node to start iteration with

    # Locate parent `p` to "attach" a new node to, while satisfying BST properties
    while q is not None:
        p = q  # Keep a trailing pointer to a parent
        if z.key == q.key:
            raise ValueError("Duplicate keys")
        elif z.key < q.key:
            q = q.left
        elif z.key > q.key:
            q = q.right
    z.parent = p  # `p` will remain None if new node is a root
    if p is None:
        T.root = z  # Tree was empty
    elif z.key < p.key:
        p.left = z
    elif z.key > p.key:
        p.right = z


def transplant(T, u, v):
    """
    Replaces one subtree as a child of its parent with another subtree.
     This utility method helps moving subtrees around and does not maintain
     BST properties, and does not update `v` child sub-trees, although it swaps
     relationship with `u`'s parent node (if not empty).

    Complexity: O(1).
    :param BST T: BST to update
    :param Node u: Node to be replaced
    :param Node v: Node to replace `u` with. Can be None
    :return None: Dynamic set of BST `T` is mutated in the process
    """
    if u.parent is None:        # Node `u` is a root
        T.root = v
    elif u == u.parent.left:    # Node `u` is a left child of its parent
        u.parent.left = v
    else:                       # Node `u` is a right child of its parent
        u.parent.right = v
    if v is not None:           # `u`'s parents become `v`'s parents
        v.parent = u.parent


def tree_delete(T, z):
    """
    Deletes a given node `z` from a BST `T` maintaining BST properties. This
     algorithm organizes its cases according to node location in a tree. These
     cases are described in detail in inline comments.

    Complexity: O(h) where `h` is the height of a tree.
    :param BST T: BST to update
    :param Node z: Node to be deleted
    :return None: Dynamic set of BST `T` is mutated in the process
    """
    # 1. If `z` has only right child, then it's removed and replaced by its
    # right child. `z`'s right child can be a leaf or None (handled by
    # `transplant()` method. Right child's own children are "taken" with him.
    if z.left is None:
        transplant(T, z, z.right)

    # 2. If `z` has only left child, we replace `z` by its left child,
    # similarly to case 1.
    elif z.right is None:
        transplant(T, z, z.left)

    # 3. Otherwise `z` has both left and right child. We find `z` successor
    # (leftmost element in `z` right subtree. We want to splice it out and
    # have it replace `z` in the tree.
    else:
        y = tree_minimum(z.right)  # `z`'s successor

        # 3a. Successor `y` lies within `z`'s right subtree, but it's not `z`'s
        # right child. `y` needs to be detached first, then resume with the case 3b.
        if y.parent is not z:
            transplant(T, y, y.right)  # `y`'s right child takes its place
            y.right = z.right          # `z`'s right subtree becomes `y`'s right subtree
            y.right.parent = y         # `y` becomes a parent of `z`'s right subtree
        # 3b. If `y` is `z`'s right child we simply have it take `z`'s position,
        # leaving `y`'s right child unmodified.
        transplant(T, z, y)  # `y` takes `z`'s place
        y.left = z.left      # `z`'s left subtree becomes `y`'s left subtree
        y.left.parent = y    # `y` becomes a parent of `z`'s left subtree
