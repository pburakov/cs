class BinaryHeap:
    """
    Binary Heap is basic implementation of a Priority Queue based on certain
     properties of a Binary Heap. Even though the diagram of a Bin Heap looks
     like a tree, the easiest way to implement it is using a list, because the
     index of every child Node in a Binary Heap is (i * 2 + 1) for left child
     and (i * 2 + 2) for the right child given the first index starts with 0.
    Another important property of a Binary Heap determines one of the two
     variations of it:
      1. Root object (index 0) of max heap is always the highest value.
      2. Root object of min heap is always the lowest value.

    TODO: Currently works as max heap only, min heaps needs some debugging.
    """

    def __init__(self, max_heap=False):
        self.items = []
        self.max_heap = max_heap

    def add(self, n):
        self.items.append(n)
        i = self.size() - 1  # Index of a new element
        if self.max_heap is True:
            self.perc_up(i)
        else:
            self.perc_down(i)

    def delete_root(self):
        """
        When heap item is deleted, the last bottom item in the heap takes its
         place at the "root" and is being percolated down.
        """
        last_value = self.items.pop()
        root_value = self.items[0]
        self.items[0] = last_value
        if self.max_heap is True:
            if self.size() > 1:
                self.perc_up(self.next_rank(0))
        else:
            self.perc_down(self.next_rank(0))
        return root_value

    def next_rank(self, i):
        """
        Gets index of next ranked child. Useful for swapping elements.
        """
        if self.size() == 2:
            return 1
        if self.items[i * 2 + 1] > self.items[i * 2 + 2]:
            return i * 2 + 1
        else:
            return i * 2 + 2

    def prev_rank(self, i):
        """
        Gets index of correct parent. Useful for swapping elements.
        """
        if i == 1 or i == 2:
            # Root
            return 0
        if i % 2 == 0:
            # Even index - right child
            return (i - 2) // 2
        else:
            # Odd index - left child
            return (i - 1) // 2

    def perc_up(self, i):
        """
        Percolates i-th element of a Heap up to its appropriate position, being
         swapped with it's parent.
        """
        i_par = self.prev_rank(i)  # Index of a parent
        while i > 0 and self.items[i_par] < self.items[i]:
            self.items[i_par], self.items[i] = self.items[i], self.items[i_par]
            i = i_par
            i_par = (i - 1) // 2

    def perc_down(self, i):
        """
        Percolates i-th element of a Heap down to its appropriate position, being
         swapped with its next ranked child.
        """
        i_ch = self.next_rank(i)  # Index of a next child
        while i <= self.size() and self.items[i_ch] < self.items[i]:
            self.items[i_ch], self.items[i] = self.items[i], self.items[i_ch]
            i = i_ch
            i_ch = self.next_rank(i)

    def size(self):
        return len(self.items)

    def root(self):
        if self.size() > 0:
            return self.items[0]
        else:
            return None


min_heap = BinaryHeap(True)
min_heap.add(3)
min_heap.add(6)
min_heap.add(1)
min_heap.add(4)
min_heap.add(10)
min_heap.add(14)
print(min_heap.items)
print(min_heap.delete_root())
print(min_heap.items)
print(min_heap.delete_root())
print(min_heap.items)
print(min_heap.delete_root())
print(min_heap.items)
min_heap.add(2)
print(min_heap.items)
print(min_heap.delete_root())
print(min_heap.items)
print(min_heap.delete_root())
print(min_heap.items)
print(min_heap.delete_root())
print(min_heap.items)
