class Queue:
    def __init__(self, s):
        """
        Basic implementation of a FIFO structure

        This implementation uses an array (Python list) to store elements or pointers
         to elements in the queue. Additionally stored are allocated memory size, current
         count of enqueued elements and pointers to the first and the last element in
         the queue.
        :param int s: Maximum size of the queue
        """
        self.head = 0
        self.tail = 0
        self.size = s
        self.items = [None] * s  # Allocated memory for elements in the stack
        self.length = 0  # Number of currently enqueued items


def enqueue(Q, x):
    """
    Adds an element at the tail of the queue

    :param Queue Q: Instance of a queue
    :param Any x: Pointer or an instance of an element to insert into a tail of
     the queue
    :return None: Queue `Q` is updated
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
    """
    Deletes an element from the head of the queue and returns it

    :param Queue Q: Instance of a queue
    :return Any: A pointer or an instance of an element from the head of the queue
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
    """
    Returns current element at the head of the queue without deleting it

    :param Stack S: Instance of a stack
    :return Any: Pointer or an instance of an element from the top of the stack
    """
    if Q.length == 0:
        raise ValueError("Empty queue")
    else:
        return Q.items[Q.head]
