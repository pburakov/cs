"""
Stack is a dynamic set that follows **"last-in, first-out"** policy. This means that the
element deleted from the set is the one most recently inserted.

Stack can be implemented using a linked list where the head of the list is also the top of
the stack .

This implementation uses an array of size *n* to store the elements and guarantee *O(1)*
time for LIFO operations. *n* is the maximum amount of elements that the stack can hold.
Elements are never physically removed from the array. It's only the pointer to the top of
the stack, represented by an array index, that is updated. This pointer keeps elements
that are still used in the stack from being replaced by newly added elements.

The removed element is always at the top of the stack.
"""


class Stack:
    """Basic implementation of a fixed size LIFO structure.
    """

    def __init__(self, n):
        """Basic implementation of a fixed size LIFO structure.

        This implementation uses an array (Python list) to store elements or pointers to
        elements in the stack. Additionally stored are allocated memory size and a pointer
        to the current top element of the stack.

        :param int n: Maximum size of the stack.

        """
        self.top = -1
        self.size = n
        self.items = [object] * n  # Allocated memory for elements in the stack


def stack_empty(S):
    """
    Evaluates if stack instance is empty.

    Complexity:
        :math:`O(1)`.

    :param Stack S: Instance of a stack.
    :return: :data:`True` if stack does not contain any elements, :data:`False` otherwise.

    """
    if S.top == -1:
        return True
    else:
        return False


def push(S, x):
    """
    Pushes a new element into the stack.

    Exceeding allocated memory will cause a "stack overflow" error.

    Complexity:
        :math:`O(1)`.

    :param Stack S: Instance of a stack.
    :param object x: Pointer or an instance of an element to insert into stack.
    :return: :data:`None`. Stack is updated.
    """
    if S.top + 1 >= S.size:
        raise OverflowError("Stack overflow")
    S.top += 1
    S.items[S.top] = x


def pop(S):
    """
    Dereferences an element from the top of the stack and removes it.

    Attempt to pop from an empty stack will cause a "stack underflow" error.

    Complexity:
        :math:`O(1)`.

    :param Stack S: Instance of a stack.
    :return: A pointer to an element at the top of the stack.
    """
    if stack_empty(S):
        raise ValueError("Stack underflow")
    else:
        x = S.items[S.top]
        S.top -= 1
        return x


def peek(S):
    """Returns current element at the top of the stack without removing it.

    Attempt to peek at an empty stack will cause a "stack underflow" error.

    Complexity:
        :math:`O(1)`.

    :param Stack S: Instance of a stack.
    :return: A pointer to an element at the top of the stack.

    """
    if stack_empty(S):
        raise ValueError("Empty stack")
    else:
        return S.items[S.top]
