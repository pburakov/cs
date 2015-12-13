class Heap:
    """
    max_heap defines if the instance is a max-heap or min-heap.
    Root object of max heap is always the highest value.
    Root object of min heap is always the lowest value.
    """

    def __init__(self, max_heap=False):
        self.items = []
        self.max_heap = max_heap

    def add(self, n):
        """
        child node index is i*2+1 for left child and i*2+2 for the right child
        """
        self.items.append(n)
        new_i = len(self.items) - 1
        parent_i = (new_i - 1) // 2
        if self.max_heap is True:
            while new_i > 0 and self.items[parent_i] < self.items[new_i]:
                self.items[parent_i], self.items[new_i] = self.items[new_i], self.items[parent_i]
                new_i = parent_i
                parent_i = (new_i - 1) // 2
        else:
            while new_i > 0 and self.items[parent_i] > self.items[new_i]:
                self.items[parent_i], self.items[new_i] = self.items[new_i], self.items[parent_i]
                new_i = parent_i
                parent_i = (new_i - 1) // 2

    def size(self):
        return len(self.items)

    def root(self):
        if len(self.items) > 0:
            return self.items[0]
        else:
            return None
