"""
Queue of Two Stacks
===================

Implement a queue using two stacks. Queue has to support `enqueue` and `dequeue`
operations.

"""


class QueueTwoStacks:
    """Implementation of a Queue using two stacks.

    Implementation details: Let stack 1 serve as a main storage. Let stack 2 be used as an
    auxiliary storage that we're going to use to rearrange items on dequeue. To keep aux
    stack from redundant rearrangement, store a flag that it's safe to use it.

    Stacks are implemented using Python lists (to save us some coding time).
    :func:`append()` and :func:`pop()` operations are :math:`O(1)`.

    """

    def __init__(self):
        self.main = []
        self.aux = []
        self.use_aux = False

    def enqueue(self, x):
        """Puts new item into the queue.

        Complexity:
            :math:`O(n)` where :math:`n` is the current number of items in the queue.

        :param object x: Object to insert

        """
        if self.use_aux is True:  # Rearrangement is required
            n = len(self.aux)
            self.main.clear()
            for i in range(n - 1, -1, -1):  # Rearranging in reverse order
                self.main.append(self.aux[i])
        self.main.append(x)
        self.use_aux = False

    def dequeue(self):
        """Removes an item from the head of the queue and returns it.

        Complexity:
            :math:`O(n)` where :math:`n` is the current number of items in the queue.

        :return: Pointer to a removed object.

        """
        n = len(self.main)
        if self.use_aux is False:  # Rearrangement is required
            self.aux.clear()
            for i in range(n - 1, -1, -1):  # Rearranging in reverse order
                self.aux.append(self.main[i])
        # Now it's safe to use aux for the next operation unless enqueue() is invoked
        self.use_aux = True
        x = self.aux.pop()
        return x
