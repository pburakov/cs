class Stack:
    """
    Implementation of Stack (last in first out) data type.

    Stack:
        4 -> [5, 6, 7]
        4 <- [4, 5, 6, 7]

    """

    def __init__(self, items=[]):
        self.items = list(items)

    def add(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
