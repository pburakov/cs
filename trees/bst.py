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
 perfectly complete and balanced, `h` will be log(n). In worst case with all the
 nodes on one side, BST will resemble a linked list and take O(n) as its height
 will be proportional to the number of elements.

There are many kinds of self-balanced BSTs, that maintain balanced tree structure.
 Most commonly mentioned are AVL tree and red-black tree but there are many other
 instances.
"""
from trees.binary_tree import BinaryTree
from trees.binary_tree import Node as BinaryTreeNode


class BST(BinaryTree):
    """
    Similar to a regular BinaryTree, holds a pointer to the root node.
    """
    pass


class Node(BinaryTreeNode):
    def __init__(self, key):
        """
        Augmented variant of a BinaryTreeNode with a pointer to its parent.

        :param Any key: Node's value (key)
        """
        super().__init__(key)
        self.parent = None


def tree_search(x, k):
    """
    Recursive search query algorithm for finding a key in BST.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node x: Node to start the search with
    :param Any k: A key (value) to search
    :return: Any: A found node or None if key `k` was not found in the tree
    """
    if x is None or x.key == k:
        return x
    elif k < x.key:
        return tree_search(x.left, k)
    elif k > x.key:
        return tree_search(x.right, k)


def iterative_tree_search(x, k):
    """
    Iterative version of BST search algorithm.

    Iterative search is more efficient on most computers due to reduced use of
     a memory stack.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node x: Node to start the search with
    :param Any k: A key (value) to search
    :return: Any: A found node or None if key `k` was not found in the tree
    """
    while k is not None and k != x.key:
        if k < x.key:
            x = x.left
        elif k > x.key:
            x = x.right
    return x


def tree_minimum(x):
    """
    Returns a pointer to a node holding a minimum value (key).

    According to BST properties it is the leftmost node in a tree.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node x: Node to start the lookup
    :return: Node: Node holding minimum value
    """
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    """
    Returns a pointer to a node holding a maximum value (key).

    According to BST properties it is the rightmost node in a tree.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node x: Node to start the lookup
    :return: Node: Node holding maximum value
    """
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):
    """
    Returns successor of a node `x`.

    Successor is a next node, determined by a sorted in-order tree traversal.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node x: Node to start the lookup
    :return Any: Will return successor node if it exists, None otherwise
    """
    if x.right is not None:
        # Return minimum element (leftmost node) in a right subtree --
        return tree_minimum(x.right)
    else:
        # -- or, if there is no right child, go up the tree from `x` until
        # we encounter a node that is the left child of its parent.
        p = x.parent
        while p is not None and x == p.right:
            x = p
            p = p.parent
        return p


def tree_predecessor(x):
    """
    Returns predecessor of a node `x`.

    Predecessor is a previous node, determined by a sorted in-order tree traversal.

    Complexity: O(h) where `h` is the height of a tree.
    :param Node x: Node to start the lookup
    :return Any: Will return predecessor node if it exists, None otherwise
    """
    if x.left is not None:
        # Return maximum element (rightmost node) in a left subtree --
        return tree_maximum(x.left)
    else:
        # -- or, if there is no left child, go up the tree from `x` until
        # we encounter a node that is the right child of its parent
        p = x.parent
        while p is not None and x == p.left:
            x = p
            p = p.parent
        return p


def tree_insert(T, z):
    """
    Inserts a new node into BST.

    The node is inserted in such a way, that the properties of BST continue to
     hold. This algorithm is similar to `tree_search()` and can also be
     implemented recursively.

    Complexity: O(h) where `h` is the height of a tree, worst case log(n).
    :param BST T: Instance of a BST to update
    :param Node z: New node, holding unique value (key)
    :return None: BST `T` is updated
    """
    p = None  # Pointer to a parent of a `z` node.
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

    This simple utility method only helps moving subtrees around. It does not
     maintain BST properties, and does not update `v` child sub-trees. It only
     maintains appropriate relations for parents of replaced nodes (if exists).

    Complexity: O(1).
    :param BST T: Instance of a BST to update
    :param Node u: Node to be replaced
    :param Node v: Node to replace `u` with. Can be None
    :return None: Dynamic set of BST `T` is mutated in the process
    """
    if u.parent is None:      # Node `u` is a root
        T.root = v
    elif u == u.parent.left:  # Node `u` is a left child of its parent
        u.parent.left = v
    else:                     # Node `u` is a right child of its parent
        u.parent.right = v
    if v is not None:         # `u`'s parents become `v`'s parents
        v.parent = u.parent


def tree_delete(T, z):
    """
    Removes a node from a BST maintaining BST properties.

    This algorithm organizes its cases according to node location in a tree.
     These cases are described in detail in inline comments.

    Complexity: O(h) where `h` is the height of a tree, worst case log(n).
    :param BST T: Instance of a BST to update
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
            y.right.parent = y         # ...and `y` becomes a parent of `z`'s right subtree

        # 3b. If `y` is `z`'s right child we simply have it take `z`'s position,
        # leaving `y`'s right child unmodified.
        transplant(T, z, y)  # `y` takes `z`'s place
        y.left = z.left      # `z`'s left subtree becomes `y`'s left subtree
        y.left.parent = y    # ...and `y` becomes a parent of `z`'s left subtree


def left_rotate(T, x):
    """
    Left rotation of a tree around pivot node `x`.

    Rotation algorithm switches node pointers around so that the tree is rotated
     counter-clockwise around `x`. Rotation is performed locally, assuming that `x`
     has a right child.

    Order of operations is important so that no pointers are lost in the process. The
     method is accompanied by step-by-step inline comments to help remember these.
     In-order traversal of a tree should remain the same after rotation, thus
     proving that rotation did not damage BST properties.

    Complexity: O(1), only pointers are changed, other attributes of a node remain
     the same.
    :param BST T: Instance of a BST to update
    :param Node x: Node to pivot the tree around
    :return None: Dynamic set of BST `T` is mutated in the process
    """
    if x.right is None:
        raise ValueError("Node has no right child")

    y = x.right               # let `y` be `x`'s right subtree, it will change places with `x`

    x.right = y.left          # `y`'s left subtree becomes `x`'s right subtree
    if y.left is not None:
        y.left.parent = x     # and `x` becomes a parent of `y`'s left subtree (if it exists)
    y.parent = x.parent       # `x`'s old parent becomes `y`s parent
    if x.parent is None:      # `y` will become the root if `x` had no parent
        T.root = y
    elif x == x.parent.left:  # `y` will be adopted by `x`'s parents depending on
        x.parent.left = y
    else:                     # ...which child was `x` (left or right)
        x.parent.right = y
    y.left = x                # `x` becomes `y`'s child
    x.parent = y              # ...and `y` becomes its parent


def right_rotate(T, x):
    """
    Right rotation of a tree around pivot node `x`.

    The code is symmetrical to `left_rotate()`.

    Complexity: O(1), only pointers are changed, other attributes of a node remain
     the same.
    :param BST T: Instance of a BST to update
    :param Node x: Node to pivot the tree around
    :return None: Dynamic set of BST `T` is mutated in the process
    """
    if x.left is None:
        raise ValueError("Node has no left child")
    y = x.left
    x.left = y.right
    if y.right is not None:
        y.right.parent = x
    y.parent = x.parent
    if x.parent is None:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y
