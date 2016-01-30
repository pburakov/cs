class Node:
    def __init__(self, value):
        self.value = value


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

    This class contains common methods for max and min heap.
    """

    def __init__(self):
        self.items = []

    def move_up(self, i):
        """ Moves i-th node one level up by flipping adjacent nodes """
        if i > 0:
            self.items[i], self.items[i - 1] = self.items[i - 1], self.items[i]

    def move_down(self, i):
        """ Moves i-th node one level down by flipping adjacent nodes """
        if i + 1 < len(self.items) - 1:
            self.items[i], self.items[i + 1] = self.items[i + 1], self.items[i]

    def perc_up(self, i):
        """
         Percolates i-th node up unless its value is lower and the name is lexicographically
         smaller than the previous position
        """
        while i > 0:
            if self.items[i].value > self.items[i - 1].value:
                self.move_up(i)
            elif self.items[i].value == self.items[i - 1].value:
                self.move_up(i)
            else:
                break
            i -= 1

    def perc_down(self, i):
        """
         Percolates i-th node down unless its value is higher and the name is lexicographically
         larger than the next position
        """
        while i < len(self.items) - 1:
            if self.items[i].value < self.items[i + 1].value:
                self.move_down(i)
            elif self.items[i].value == self.items[i + 1].value:
                self.move_down(i)
            else:
                break
            i += 1

    def __str__(self):
        return str([item.value for item in self.items])
