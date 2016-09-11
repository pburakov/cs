"""
Queue is a dynamic set that follows "first-in, first-out" policy. This means that the
 element deleted from the set is the one that have been in the queue for the longest
 time.

Query can be implemented using a doubly linked list using pointers to the head and
 the tail of the list as the head and the tail of the queue.

This implementation uses an array of size `n` to store the elements. `n` is the
 maximum amount of elements that the queue can hold. Elements are never physically
 removed from the array. Only pointers to the head and the tail of the queue,
 represented by array indices, are shifted. Pointers keep elements that are still
 used in the queue from being replaced by newly added elements.

Keeping track of a quantity of currently enqueued elements helps making sure that
 the allocated size is never exceeded. In some sense, this representation of a queue
 resembles a snake chasing its own tail.

Like a newly arriving customer takes a place in the line, the enqueued element is
 added at the tail of the queue. And like the customer at the head of the line, the
 de-queued element is always at the head of a queue.
"""


class Queue:
    def __init__(self, n):
        """
        Basic implementation of a fixed size FIFO structure.

        This implementation uses an array (Python list) to store elements or pointers
         to elements in the queue. Additionally stored are allocated memory size, current
         count of enqueued elements and pointers to the first and the last element in
         the queue.

        :param int n: Maximum size of the queue
        """
        self.head = 0
        self.tail = 0
        self.size = n
        self.items = [object] * n  # Allocated memory for elements in the queue
        self.length = 0  # Number of currently enqueued items


def enqueue(Q, x):
    """
    Adds an element at the tail of the queue.

    Exceeding allocated memory will cause a "queue overflow" error.

    Complexity: O(1)
    :param Queue Q: Instance of a queue
    :param object x: Pointer or an instance of an element to insert into a tail of
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
    Dereferences an element from the head of the queue and returns it.

    Attempt to dequeue from an empty queue will cause a "queue underflow" error.

    Complexity: O(1)
    :param Queue Q: Instance of a queue
    :return Any: A pointer or an instance of an element at the head of the queue
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
    Returns current element at the head of the queue without removing it.

    Attempt to lookup next element in an empty queue will cause an "empty queue"
     error.

    Complexity: O(1)
    :param Queue Q: Instance of a queue
    :return Any: Pointer or an instance of an element at the head of the queue
    """
    if Q.length == 0:
        raise ValueError("Empty queue")
    else:
        return Q.items[Q.head]


"""
Stack is a dynamic set that follows "last-in, first-out" policy. This means that the
 element deleted from the set is the one most recently inserted.

Stack can be implemented using a linked list where the head of the list is also the top
 of the stack .

This implementation uses an array of size `n` to store the elements and guarantee O(1)
 access time. `n` is the maximum amount of elements that the stack can hold. Elements
 are never physically removed from the array. It's only the pointer to the top of the
 stack, represented by an array index, that is updated. This pointer keeps elements
 that are still used in the stack from being replaced by newly added elements.

The removed element is always at the top of the stack.
"""


class Stack:
    def __init__(self, n):
        """
        Basic implementation of a fixed size LIFO structure.

        This implementation uses an array (Python list) to store elements or pointers
         to elements in the stack. Additionally stored are allocated memory size and
         a pointer to the current top element of the stack.

        :param int n: Maximum size of the stack
        """
        self.top = -1
        self.size = n
        self.items = [object] * n  # Allocated memory for elements in the stack


def stack_empty(S):
    """
    Evaluates if stack instance is empty.

    Complexity: O(1)
    :param Stack S: Instance of a stack
    :return bool: True if stack does not contain any elements, False otherwise
    """
    if S.top == -1:
        return True
    else:
        return False


def push(S, x):
    """
    Pushes a new element into the stack.

    Exceeding allocated memory will cause a "stack overflow" error.

    Complexity: O(1)
    :param Stack S: Instance of a stack
    :param object x: Pointer or an instance of an element to insert into stack
    :return None: Stack `S` is updated
    """
    if S.top + 1 >= S.size:
        raise OverflowError("Stack overflow")
    S.top += 1
    S.items[S.top] = x


def pop(S):
    """
    Dereferences an element from the top of the stack and removes it.

    Attempt to pop from an empty stack will cause a "stack underflow" error.

    Complexity: O(1)
    :param Stack S: Instance of a stack
    :return Any: Pointer or an instance of an element at the top of the stack
    """
    if stack_empty(S):
        raise ValueError("Stack underflow")
    else:
        x = S.items[S.top]
        S.top -= 1
        return x


def peek(S):
    """
    Returns current element at the top of the stack without removing it.

    Attempt to peek at an empty stack will cause a "stack underflow" error.

    Complexity: O(1)
    :param Stack S: Instance of a stack
    :return Any: Pointer or an instance of an element at the top of the stack
    """
    if stack_empty(S):
        raise ValueError("Empty stack")
    else:
        return S.items[S.top]
