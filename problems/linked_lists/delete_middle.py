"""
Delete Middle Node
==================

Implement an algorithm to delete a node in the middle (any node but the first and last node)
of a singly linked list, given only a pointer to that node.

Example::

    ([a->b->c->d->e], c) -> [a->b->d->e]
"""

from basic.linked_list import Node


def delete_middle(x):
    """Deletes a middle node from a singly linked list.

    The solution is to copy the key from the next node and switch the pointer to the
    next's next node.

    Complexity:
        :math:`O(1)`.

    :param Node x: Node to delete.

    """
    next = x.next
    x.key = next.key
    x.next = next.next
