class BinaryHeap:
    """
    Binary Heap is basic implementation of a priority queue based on certain
     properties of a Binary Heap. Even though the diagram of a Bin Heap looks
     like a tree, the easiest way to implement it is using a list, because the
     index of every child Node in a Binary Heap is (i * 2 + 1) for left child
     and (i * 2 + 2) for the right child given the first index starts with 0.
    Another important property of a Binary Heap determines one of the two
     variations of it:
      1. Root object of max heap is always the highest value.
      2. Root object of min heap is always the lowest value.
    """

    def __init__(self, max_heap=False):
        self.items = []
        self.max_heap = max_heap

    def add(self, n):
        self.items.append(n)
        i = len(self.items) - 1
        i_par = (i - 1) // 2  # Index of a parent
        if self.max_heap is True:
            while i > 0 and self.items[i_par] < self.items[i]:
                self.items[i_par], self.items[i] = self.items[i], self.items[i_par]
                i = i_par
                i_par = (i - 1) // 2
        else:
            while i > 0 and self.items[i_par] > self.items[i]:
                self.items[i_par], self.items[i] = self.items[i], self.items[i_par]
                i = i_par
                i_par = (i - 1) // 2

    def size(self):
        return len(self.items)

    def root(self):
        if self.size() > 0:
            return self.items[0]
        else:
            return None


min_heap = BinaryHeap()
min_heap.add(3)
min_heap.add(5)
min_heap.add(8)
min_heap.add(2)
min_heap.add(9)
min_heap.add(13)
print(min_heap.items)
