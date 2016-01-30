from trees.binary_heap import BinaryHeap
from trees.binary_heap import Node


class MaxHeap(BinaryHeap):
    """
     Priority queue / max-heap like data structure, implemented using a list.
     Slightly optimized add() method. Guarantees that values are ordered on addition.
    """

    def add(self, value):
        node = Node(value)

        # Value list is empty, O(1).
        if not self.items:
            self.items.append(node)

        # Value is higher than top value, O(n), n is the current number of names in the rating.
        elif node.value > self.items[0].value:
            self.items.insert(0, node)

        # Value is equal to the top value,
        # complexity is O(n*k), where k is number of names with the same value.
        elif node.value == self.items[0].value:
            self.items.insert(0, node)
            self.perc_down(0)

        # Value is less than the bottom value, O(1).
        elif node.value < self.items[-1].value:
            self.items.append(node)

        # Value is equal to the bottom value or is somewhere in the middle,
        # complexity is O(k), where k is how far the value is from the bottom position (k -> n)
        else:
            self.items.append(node)
            self.perc_up(len(self.items) - 1)


max_heap = MaxHeap()
max_heap.add(3)
max_heap.add(6)
max_heap.add(1)
max_heap.add(4)
max_heap.add(10)
max_heap.add(14)
print(max_heap)
max_heap.add(2)
print(max_heap)
