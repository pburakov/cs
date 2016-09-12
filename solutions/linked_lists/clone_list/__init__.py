def clone(L):
    """
    Solution of cloned list problem.

    Somewhat more easy-to-read solution involves storage of pointers in a hash table,
     which gives O(n) time, but O(n) additional spce as well. The following algorithm only
     performs pointer operations in place and doesn't consume any additional memory
     (besides memory to allocate the cloned list itself).

    The principle is simple. In the first run, we insert cloned nodes in between original
     nodes and assigning them as next nodes in the list. This will make the list twice
     its original length, with every first node to be an original one, and every second
     one to be a clone. Second run clones secondary pointers by shifting them one position
     ahead. Finally we do a third run, rearranging next node pointers to match the list
     they belong to.

    Complexity: O(n), three O(n) runs still give linear growth
    :param List L: Original list
    :return List: Cloned list
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
    def __init__(self, key):
        """
        Node of a singly linked list containing arbitrary pointer.

        :param object key:
        """
        self.key = key
        self.next = None
        self.other = None

    def __str__(self):
        return str(self.key)


class List:
    def __init__(self):
        """
        Singly linked list implementation.
        """
        self.head = None

    def insert(self, x):
        """
        Insertion procedure.

        Complexity: O(n)
        :param Node x: Node to insert
        :return None: List is updated
        """
        x.next = self.head
        self.head = x

    def __str__(self):
        node = self.head
        out = ''
        while node:
            out += str(node)
            if node.other is not None:
                out += '(->{})'.format(str(node.other))
            out += ' '
            node = node.next
        return out
