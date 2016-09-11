# Binary Tree

Binary Tree is a linked data structure, where each node can point to two other nodes at 
 most. These nodes are called left and right **child nodes**. Nodes that don't have any
 children pointers (replaced with null pointers) are called **leafs**.

Every node in a binary tree is a **root** to its own **subtree**. This property allows the
 implementation of easy to understand recursive traversal algorithms that operate within
 a subtree of arbitrary node (not necessarily the root of a whole tree).

Traversal algorithms are called **pre-order**, **post-order** and **in-order**, so named
 because of the sequence in which the algorithm "visits" a node between the traversal of
 its left and right subtree without  mutating the node (for example printing its value on
 the screen). This operation recurs until all the nodes in a sub-tree are eventually
 "visited".

Such operations that don't change the dynamic set of a tree are called **querying**.
 Operations that cause change are called **updating**.