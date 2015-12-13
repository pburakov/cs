class Deque:
    """
    Deque implementation using python list.

    Deque:
        4 -> [5, 6, 7] <- 8
        4 <- [4, 5, 6, 7, 8] -> 8

    Deque is a double-sided queue. Items can be appended and removed from both
     sides of the queue. Rear side is the beginning of the list so add_rear()
     and remove_rear() have complexity of O(n). Front operations are O(1).

    """

    def __init__(self, items=[]):
        self.items = list(items)

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
