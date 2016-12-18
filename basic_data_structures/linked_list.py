"""
Linked List
===========

Linked list is a simple data structure in which the objects are arranged in a linear
order. Unlike an array, however, in which elements are ordered by the array indices,
linked list is ordered using pointers in each object. Linked list provides a simple,
flexible, although not very efficient, representation for dynamic sets.

Every node of a basic linked list holds some data, called the **key** and a reference to
the **next** element. Last element of the singly linked list points to a null object. Head
of the list points to a first object in the list. In order to find an element with a given
key, the list has to be searched starting at the head.

There are various kinds of linked lists. For instance, the last element of a **circular
list** has no null pointer. Instead it points to the head element, effectively making a
loop. Ordered linked lists offer certain advantages in searching, but increase the cost
for inserting. This is an implementation of a **doubly linked** list where every element
additionally holds a reference to a previous element.

Please note, that Python `list` is not implemented as a linked list. Internally Python
lists are dynamic arrays (implemented as a vector of pointers).
"""


class Node:
    """Node of a doubly linked list.
    """

    def __init__(self, key):
        """Node of a doubly linked list.

        Has a value and two pointer attributes: the next and previous adjacent element in
        the list.

        :param object key: Node's key.

        """
        self.key = key
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.key)


class LinkedList:
    """Basic implementation of a doubly linked list, holds a pointer to its head.
    """

    def __init__(self):
        self.head = None

    """
    Python implementation for linked list iteration
    """

    def __iter__(self):
        self.p = self.head  # Iteration pointer
        return self

    def __next__(self):
        if self.p is None:
            raise StopIteration
        else:
            x = self.p
            self.p = self.p.next
            return x


def list_search(L, k):
    """Finds the first element with a given key in a linked list.

    Complexity:
        :math:`O(n)`, in worst case the entire list will be searched if an element with a
        given key is not present in the list.

    :param LinkedList L: An instance of a linked list.
    :param object k: A key to search.
    :return: A pointer to a element or :data:`None` if key was not found.

    """
    x = L.head
    while x is not None and x.key != k:
        x = x.next
    return x


def list_insert(L, x):
    """Inserts a new node at the head of a doubly linked list.

    Complexity:
        :math:`O(1)`, only the head pointer of a list is updated.

    :param LinkedList L: An instance of a doubly linked list.
    :param Node x: Pointer to a new doubly linked list node to insert.

    """
    x.next = L.head
    if L.head is not None:
        L.head.prev = x
    L.head = x
    x.prev = None


def list_delete(L, x):
    """Removes a node from a doubly linked list.

    Complexity:
        :math:`O(1)`, for a known node, since only the pointers are removed.

    :param LinkedList L: An instance of a doubly linked list.
    :param Node x: Pointer to a doubly linked list node to remove.

    """
    if x.prev is not None:
        x.prev.next = x.next
    else:
        L.head = x.next
    if x.next is not None:
        x.next.prev = x.prev
