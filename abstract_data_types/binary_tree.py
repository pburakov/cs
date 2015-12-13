class BinaryTree:
    """
    Binary Tree is a simple Tree object, where each Node can have no more than
     two Children nodes. Each Node holds some value and a reference to its Children,
     which in their turns are the Root Node for a Binary Tree down one level.
    """

    def __init__(self, value):
        """
        Instantiates a tree object with a content and empty Children references.
        """
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        """
        Places a child node to an empty slot or pushes an existing child
         down one level. By swapping the link between the two objects.
        """
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child, self.left_child = self.left_child, new_node

    def insert_right(self, value):
        """
        Symmetric to insert_left().
        """
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child, self.right_child = self.right_child, new_node
