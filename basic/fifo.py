"""
Queue
=====

Queue is a dynamic set that follows **"first-in, first-out"** policy. This means that the
element deleted from the set is the one that have been in the queue the longest time.

Like a newly arriving customer takes a place in the line, the enqueued element is added at
the tail of the queue. And like the customer at the head of the line, the de-queued
element is always at the head of a queue.

Queue can be implemented using a doubly linked list with pointers to the head as the head
of the queue and a tail of the list as the tail of the queue.

"""


class Queue:
    """Basic implementation of a fixed size FIFO structure.

    This implementation uses an array of size :math:`n` to store the elements. :math:`n` is
    the maximum amount of elements that the queue can hold. Elements are never being
    removed from the array; only the pointers to the head and the tail of the queue,
    represented by array indices, are shifted. Pointers help elements that are still used
    in the queue from being replaced by newly added elements.

    Keeping track of the quantity of enqueued elements helps makes sure that the
    allocated size is never exceeded. In some sense, this representation of a queue
    resembles a snake chasing its own tail.
    """

    def __init__(self, n):
        """Basic implementation of a fixed size FIFO structure.

        :param int n: Maximum size of the queue.

        """
        self.head = 0  # Index of head
        self.tail = 0  # Index of tail
        self.size = n  # Max size
        self.length = 0  # Number of currently enqueued items
        self.items = [None] * n  # Allocated memory for elements in the queue


def enqueue(Q, x):
    """Adds an element at the tail of the queue.

    Exceeding allocated memory will cause a "queue overflow" error.

    Complexity:
        :math:`O(1)`.

    :param Queue Q: Instance of a queue.
    :param object x: An element to insert at a tail of the queue.

    """
    if Q.length == Q.size:
        raise OverflowError("Queue overflow")
    Q.items[Q.tail] = x
    if Q.tail + 1 >= Q.size:
        Q.tail = 0
    else:
        Q.tail += 1
    Q.length += 1


def dequeue(Q):
    """Dereferences an element from the head of the queue and returns it.

    Attempt to dequeue from an empty queue will cause a "queue underflow" error.

    Complexity:
        :math:`O(1)`.

    :param Queue Q: Instance of a queue.
    :return: Removed element.

    """
    if Q.length == 0:
        raise ValueError("Queue underflow")
    x = Q.items[Q.head]
    if Q.head + 1 >= Q.size:
        Q.head = 0
    else:
        Q.head += 1
    Q.length -= 1
    return x


def next(Q):
    """Returns current element at the head of the queue without removing it.

    Attempt to lookup an element in an empty queue will cause an "empty queue" error.

    Complexity:
        :math:`O(1)`.

    :param Queue Q: Instance of a queue.
    :return: An element at the head of the queue.

    """
    if Q.length == 0:
        raise ValueError("Empty queue")
    else:
        return Q.items[Q.head]
