class Node:
    def __init__(self, key):
        """
        Node of a doubly linked list.

        Has a value and two pointer attributes: the next and previous adjacent element
         in the list.

        :param object key: Node's value (key)
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
    """
    Finds the first element with a given key in a linked list.

    Complexity: O(n), in worst case the entire list will be searched if an element
     with a given key is not present in the list.
    :param LinkedList L: An instance of a linked list
    :param object k: A key (value) to search
    :return Any: Pointer to a element or None if key was not found
    """
    x = L.head
    while x is not None and x.key != k:
        x = x.next
    return x


def list_insert(L, x):
    """
    Inserts a new node at the head of a doubly linked list.

    Complexity: O(1), only the head pointer of a list is updated
    :param LinkedList L: An instance of a doubly linked list
    :param Node x: Pointer to a new doubly linked list node to insert
    :return None: List `L` is mutated
    """
    x.next = L.head
    if L.head is not None:
        L.head.prev = x
    L.head = x
    x.prev = None


def list_delete(L, x):
    """
    Removes a node from a doubly linked list.

    Complexity: O(1), for a known node, since only the pointers are removed. It will
     take additional O(n) time to find an arbitrary node.
    :param LinkedList L: An instance of a doubly linked list
    :param Node x: Pointer to a doubly linked list node to remove
    :return None: List `L` is mutated
    """
    if x.prev is not None:
        x.prev.next = x.next
    else:
        L.head = x.next
    if x.next is not None:
        x.next.prev = x.prev
