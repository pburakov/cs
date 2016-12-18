"""
Clone List with Arbitrary Pointer
=================================

Given singly linked list consisting of elements that have a second pointer pointing to an
arbitrary node in the same list, write an efficient function to deeply clone it.

Node structure for reference::

    template<typename T>
    struct Node {
        T key;
        Node *next;
        Node *other;
    };

"""


def solution(L):
    """Solution of cloned list problem.

    In an interview with a company I've been suggested to use a map to store pointers (I'm
    assuming keyed by their in-memory address) in a somewhat "brute-force" solution. It
    gives :math:`O(n)` time, but uses :math:`O(n)` additional space as well. The following
    algorithm only performs pointer operations in place and doesn't consume any additional
    memory (besides memory to allocate the cloned list itself).

    The principle is simple. In the first run, we insert cloned nodes in between original
    nodes and assigning them as next nodes in the list. This will make the list twice its
    original length, with every first node to be an original one, and every second one to
    be a clone. Second run clones secondary pointers by shifting them one position ahead.
    Finally we do a third run, rearranging next node pointers to match the list they
    belong to.

    When solving this problem (an other linked-list related problems), make sure to draw
    out the solution on paper or a whiteboard first, since it's very easy to lose track of
    pointer operations.

    Complexity:
        :math:`O(n)`, three :math:`O(n)` runs still give linear growth.

    :param List L: Original list.
    :return: Cloned list.

    """
    cloned_head = None
    # First run (cloning nodes)
    p = L.head
    while p:
        cloned_node = Node(p.key)
        if cloned_head is None:  # Remembering the head of the cloned list
            cloned_head = cloned_node
        original_next = p.next
        cloned_node.next = original_next
        p.next = cloned_node
        p = original_next
    # Second run (cloning secondary pointers)
    p = L.head
    while p:
        cloned_node = p.next
        if p.other is not None:
            cloned_node.other = p.other.next
        original_next = cloned_node.next
        p = original_next
    # Third run (rearranging pointers)
    p = L.head
    while p:
        original_node = p
        cloned_node = p.next
        p = cloned_node.next
        original_node.next = cloned_node.next
        if original_node.next is not None:
            cloned_node.next = original_node.next.next
        else:
            cloned_node.next = None
    out = List()
    out.head = cloned_head
    return out


"""
Data structures used in the solution
"""


class Node:
    """Node of a singly linked list containing arbitrary pointer.
    """

    def __init__(self, key):
        self.key = key
        self.next = None
        self.other = None

    def __str__(self):
        return str(self.key)


class List:
    """Singly linked list implementation.
    """

    def __init__(self):
        self.head = None

    def insert(self, x):
        x.next = self.head
        self.head = x

    def __str__(self):
        node = self.head
        out = ''
        while node:
            out += str(node)
            if node.other is not None:
                out += "(^{})".format(str(node.other))
            out += " -> "
            node = node.next
        out += "null"
        return out
