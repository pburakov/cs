# Binary Search Tree

BST (Binary Search Tree) is a convenient binary tree data structure that allows fast 
 value lookup. Basic operations on a complete BST take time proportional to a **height** 
 of a tree rather that the number of its elements.

The values (or **keys** as named in CLRS) in a BST are stored in such a way as to satisfy
 the main BST property. For any **parent node** in a BST, its left child must hold a 
 smaller value and its right child must hold a bigger value.

Every node in a binary tree is a **root** to its own **subtree**. Inductively, BST 
 property guarantees that any value in a left subtree will be smaller than the root node
 and any value in a right subtree will be bigger.

**In-order** printing of nodes in a BST will produce sorted output of its values. Nodes
 in augmented BSTs can hold more properties and offer more efficient operations in a 
 handful of applications.

The correctness of these algorithms is guaranteed by the BST properties. Notice that the
 update algorithms implemented here, such as `tree_insert()`, `transplant()` and 
 `tree_delete()` (algorithms that cause the dynamic set represented by BST to change)
 operate on an instance of BST, while query algorithms operate on arbitrary nodes.

Most BST operations take *O(h)* time where *h* is a height of a tree. If tree is perfectly
 complete and **balanced**, *h* will be *log(n)*. In worst case with all the nodes on one 
 side, BST will resemble a linked list and take *O(n)* as its height will be proportional
 to the number of elements.

There are many kinds of self-balanced BSTs, that maintain balanced tree structure. Most
 commonly mentioned are AVL tree and red-black tree but there are many other instances.
 
###See code:
- [Binary Search Tree](./__init__.py)