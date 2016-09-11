# AVL Tree

AVL tree (Adelson-Velsky-Landis tree) is a height-based self-balancing binary search tree.

Besides regular BST properties, AVL tree keeps the heights of the two child subtrees of 
 any node differ by at most one. Simple formulae for node height and a balance factor 
 (see code for `update_height()` and `balance_factor()`) help maintain its representation
 invariant.

Rebalancing is performed by one or more tree rotations on every update of a dynamic set,
 such as insertion and deletion of a node. Balanced tree structure guarantees node lookup,
 insertion and deletion in O(log(n)) time.

Augmented BST structure stores height attribute in every node in order to reduce the
 number of height computations.
