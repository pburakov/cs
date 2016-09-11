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