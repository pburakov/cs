class Queue:
    """
    Implements Queue (first in first out) abstract data type

    4 -> [5, 6, 7]
    [4, 5, 6, 7] -> 7

    In this implementation the complexity of enqueue() is O(n), and dequeue()
      is O(1), but it's possible to implement the other way around.
    """

    def __init__(self, items=[]):
        self.items = list(items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []
