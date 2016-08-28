"""
Implement a queue using two stacks.
"""


class Queue:
    def __init__(self):
        """
        Implementation of a Queue using two stacks.

        Implementation details: Let stack 1 serve as a main storage. Let stack 2 be used
         as an auxiliary storage that we're going to use to rearrange items on dequeue.
         To keep aux stack from redundant rearrangement, store a flag that it's safe to
         use it.

        Stacks are implemented using Python lists (to save us some coding time).
         `append()` and `pop()` operations are O(1).
        """
        self.main = []
        self.aux = []
        self.use_aux = False

    def enqueue(self, x):
        """
        Puts new item into the queue.

        Complexity: O(n) where `n` is the current number of items in the queue.
        :param object x: Object to insert
        :return None: Queue is updated
        """
        if self.use_aux is True:  # Rearrangement is required
            n = len(self.aux)
            self.main.clear()
            for i in range(n - 1, -1, -1):  # Rearranging in reverse order
                self.main.append(self.aux[i])
        self.main.append(x)
        self.use_aux = False

    def dequeue(self):
        """
        Removes an item from the head of the queue.

        Complexity: O(n) where `n` is the current number of items in the queue.
        :return object: Removed object.
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
