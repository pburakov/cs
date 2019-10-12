"""
Queue of Two Stacks
===================

Implement a queue using two stacks. The queue has to support :func:`enqueue()` and
:func:`dequeue()` operations.

"""


class QueueTwoStacks:
    """Implementation of a Queue using two stacks.

    Let Stack 2 act as a "snapshot" of Stack 1 at the moment when :func:`dequeue()` method
    was called. The items on Stack 2 are arranged in reverse order to emulate properties of
    FIFO structure.

    Stacks are implemented using Python lists (to save us some coding time).
    :func:`append()` and :func:`pop()` operations are :math:`O(1)`.
    """

    def __init__(self):
        """Implementation of a Queue using two stacks.
        """
        self.s1 = []
        self.s2 = []


def enqueue(Q, x):
    """Puts new item into the queue.

    Complexity:
        :math:`O(1)`.

    :param QueueTwoStacks Q: Queue.
    :param object x: Element to insert.

    """
    Q.s1.append(x)


def dequeue(Q):
    """Removes an item from the head of the queue and returns it.

    Complexity:
        :math:`O(n)`, :math:`O(1)` amortized.

    :param QueueTwoStacks Q: Queue.
    :return: Removed element.

    """
    if len(Q.s2) == 0:
        while Q.s1:  # Rearrange items in s2 in reverse order
            Q.s2.append(Q.s1.pop())
    return Q.s2.pop()
