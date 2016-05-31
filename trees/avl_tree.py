"""
AVL tree (Adelson-Velsky-Landis tree) is a height-based self-balancing binary search
 tree.

Besides regular BST properties, AVL tree keeps the heights of the two child subtrees
 of any node differ by at most one. Simple formulae for node height and a balance
 factor (see code for `update_height()` and `balance_factor()`) help maintain its
 representation invariant.

Rebalancing is performed by one of more tree rotations on every update of a dynamic set,
 such as insertion and deletion of a node. Balanced tree structure guarantees node
 lookup, insertion and deletion in O(log(n)) time.

Augmented BST structure stores height attribute in every node in order to reduce the
 number of height computations.
"""
from trees.bst import tree_insert, tree_delete
from trees.bst import right_rotate, left_rotate
from trees.bst import BST
from trees.bst import Node as BSTNode


class AVLTree(BST):
    """
    AVL tree is a self-balanced implementation of a BST
    """
    pass


class Node(BSTNode):
    def __init__(self, key):
        """
        Augmented BST node with additional height attribute.

        :param Any key: Node's value (key)
        """
        super().__init__(key)
        self.height = 0


def height(x):
    """
    Returns height attribute of a node `x`.

    Null nodes (children of leaf nodes) have a height of -1 to make a height and
     balance factor formulae work. This algorithm assumes that height attributes of
     children nodes are correct.

    Complexity: O(1)
    :param Node x: Subject node
    :return int: Height of node `x`
    """
    if x is None:
        return -1
    else:
        return x.height


def update_height(x):
    """
    Calculates and writes height attribute into node `x`.

    This algorithm assumes that height attributes of children nodes are correct.
     Null nodes have a height of -1. Leaf nodes have a height of 0.

    Complexity: O(1).
    :param Node x: Subject node
    :return None: Node `x` is mutated in the process
    """
    x.height = max(height(x.left), height(x.right)) + 1


def balance_factor(x):
    """
    Returns balance factor of node `x`.

    This algorithm assumes that height attributes of children nodes are correct.
     For a balanced node balance factor `f` must be `-1 ≤ f ≤ 1`.

    Complexity: O(1).
    :param Node x: Subject node
    :return int: Balance factor of node `x`
    """
    return height(x.left) - height(x.right)


def avl_rebalance(T, x):
    """
    Recursive AVL rebalancing.

    This algorithm implicitly assumes that AVL properties are maintained for nodes
     below `x`. Once node `x` is fixed, rebalancing will continue for `x`'s parents
     until the root of a subtree is reached and AVL properties are maintained for
     an entire subtree.

    Rebalancing has several edge cases depending on a balance factor of a node.
     Inline comments are added to the code, describing those cases. Height attributes
     of all traversed nodes are updated in the process.

    Complexity: O(log(n)). Rotations take O(1) time.
    :param AVLTree T: Instance of an AVL tree to update
    :param Node x: Node to adjust (if needed)
    :return None: Dynamic set of AVL tree `T` is mutated in the process
    """
    if x is not None:
        update_height(x)
        f = balance_factor(x)

        # 1. `x`'s right subtree is "heavier"
        if f < -1:
            a = x.right  # Pointer to `x`'s right subtree

            # 1a. Two rotations will be required when edges of `x`, `a` and `a`'s
            # heaviest child form a "zig-zag"
            if height(a.left) >= height(a.right):
                right_rotate(T, a)
                update_height(a)
                left_rotate(T, x)

            # 1b. Edges of `x`, `a` and `a`'s heaviest child form a straight line,
            # single rotation is required.
            else:
                left_rotate(T, x)
            update_height(x)  # In either cases 1a and 1b `x`'s height is updated

        # 2. `x`'s left subtree is "heavier"
        elif f > 1:
            b = x.left  # Pointer to `x`s left subtree

            # 2a. Symmetric cases for edges of `x`, `b` and `b`'s heaviest child
            if height(b.right) >= height(b.left):
                left_rotate(T, b)
                update_height(b)
                right_rotate(T, x)

            # 2b. Symmetric case for 1b.
            else:
                right_rotate(T, x)
            update_height(x)
        avl_rebalance(T, x.parent)  # Going up one level of `x`


def avl_insert(T, z):
    """
    Inserts a new node into an AVL tree.

    Rebalances `z`'s children and nodes above `z` if they disobey AVL tree property.

    Complexity: O(log(n)), O(log(n)) for lookup for an appropriate insert position
     and O(log(n)) for average rebalancing.
    :param AVLTree T: Instance of an AVL tree to update
    :param Node z: Node to insert
    :return None: Dynamic set of AVL tree `T` is mutated in the process
    """
    tree_insert(T, z)
    avl_rebalance(T, z)


def avl_delete(T, z):
    """
    Removes a node from AVL tree.

    Node is deleted in such a way so that AVL tree properties continue to hold.

    Complexity: O(log(n)), same as `avl_insert()`
    :param AVLTree T: Instance of an AVL tree to update
    :param Node z: Node to remove
    :return None: Dynamic set of AVL tree `T` is mutated in the process
    """
    p = z.parent  # Keep pointer to a parent of a deleted node
    tree_delete(T, z)
    # Other node or null will take `z`'s place. First node that is potentially
    # out of balance is `z`'s parent.
    avl_rebalance(T, p)
