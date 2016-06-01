"""
Linked list is a simple data structure in which the objects are arranged in a linear
 order. Unlike an array, however, in which elements are ordered by the array indices,
 the order in a linked list is using only pointers in each object. Linked list provide
 a simple, flexible, although not very efficient, representation for dynamic sets.

Every node of a basic linked list holds some data, called the key and a reference to
 the next element. Last element of the singly linked list points to a null object. Head
 of the list points only to a first object in the list. In order to find an element
 with a given key, the entire list has to be searched starting at the head.

There are various kinds of linked lists. For instance, the last element of a circular
 list has no null pointer. Instead it points to the head element, effectively making
 it a loop. Ordered linked lists offer certain advantages in searching, but increase
 the cost for inserting.

This is an implementation of a doubly linked list where every element additionally
 holds a reference to a previous element.

Please note, that Python list is not implemented as a linked list. Internally Python
 lists are dynamic arrays (implemented as a vector of pointers).
"""


class Node:
    def __init__(self, key):
        """
        Node of a doubly linked list.

        Has a value and two pointer attributes: the next and previous adjacent element
         in the list.

        :param Any key: Node's value (key)
        """
        self.key = key
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.key)


class LinkedList:
    def __init__(self):
        """
        Basic implementation of a doubly linked list, holds a pointer to its head.
        """
        self.head = None


def list_search(L, k):
    """
    Finds the first element with a given key in a linked list

    Complexity: O(n), in worst case the entire list will be searched if an element
     with a given key is not present in the list.
    :param LinkedList L: An instance of a linked list
    :param Any k: A key (value) to search
    :return Any|None: Found element or None if key was not found
    """
    x = L.head
    while x is not None and x.key != k:
        x = x.next
    return x


def list_insert(L, x):
    """
    Inserts a new node at the head of a doubly linked list

    Complexity: O(1), only the head pointer of a list is updated
    :param LinkedList L: An instance of a doubly linked list
    :param Node x: Pointer to a new doubly linked list node to insert
    :return None: List `L` is mutated
    """
    x.next = L.head         # Old head of a list now becomes `x`'s successor
    if L.head is not None:  # If list wasn't empty,
        L.head.prev = x     # ...maintaining pointer to the predecessor
    L.head = x              # `x` becomes a new head of the list.
    x.prev = None           # First node has no predecessor


def list_delete(L, x):
    """
    Removes a node from a doubly linked list

    Complexity: O(1), for a known node, since only the pointers are removed. It will
     take additional O(n) time to find an arbitrary node.
    :param LinkedList L: An instance of a doubly linked list
    :param Node x: Pointer to a doubly linked list node to remove
    :return None: List `L` is mutated
    """
    if x.prev is not None:    # 1. Element is somewhere near to the end of the list
        x.prev.next = x.next  # Previous item now points to `x`'s successor
    else:                     # 2. List's head is removed
        L.head = x.next       # List's head now points to `x`'s successor
    if x.next is not None:    # And if we're not at the end of the list,
        x.next.prev = x.prev  # ...maintaining pointer to the predecessor.
