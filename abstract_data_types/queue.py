from abstract_data_types.linked_list import Node as Item

class Queue:
    """
    Implements Queue (first in first out) abstract data type.

    4 -> [5, 6, 7]
    [4, 5, 6, 7] -> 7

    In this implementation the complexity of enqueue() is O(n), and dequeue()
      is O(1), but it's possible to implement the other way around.
    """

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item):
        if self.last is not None:
            self.last.next = item
        self.last = item
        if self.first is None:
            self.first = self.last

    def deque(self):
        if self.first is None:
            raise ValueError("Empty queue")
        output = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return output

    def peek(self):
        if self.first is None:
            raise ValueError("Empty queue")
        return self.first

    def is_empty(self):
        return self.first is None and self.last is None

    def __str__(self):
        next = self.first
        output = []
        while next is not None:
            output.append(next.value)
            next = next.next
        return ', '.join(output)


a = Item('a')
b = Item('b')
c = Item('c')
d = Item('d')
e = Item('e')
queue = Queue()
queue.enqueue(a)
queue.enqueue(b)
queue.enqueue(c)
queue.enqueue(d)
queue.enqueue(e)
print(queue)
print(queue.deque().value)
print(queue.deque().value)
print(queue.deque().value)
print(queue.deque().value)
print(queue.deque().value)
