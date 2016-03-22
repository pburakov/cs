class Node:
    """
    Node of a simple tree, with unlimited amount of children.
    """

    def __init__(self, value):
        self.value = value
        self.children = []
