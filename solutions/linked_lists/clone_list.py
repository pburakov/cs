"""
Given singly linked list consisting of elements that have a second pointer pointing to an arbitrary node in the same list, write an effecient function to clone it.

Node structure for reference:
```
struct Node {
  char key;
  Node next;
  Node other;
}
```
"""


def clone(L):
    """
    Solution for cloned list problem.

    Complexity: O(n)
    :param List L: Original list
    :return List: Cloned list
    """
    cloned_head = None
    # First run (cloning)
    p = L.head
    while p:
        cloned_node = Node(p.key)
        if cloned_head is None:
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


class List:
    def __init__(self):
        """
        Singly linked list implementation.
        """
        self.head = None
