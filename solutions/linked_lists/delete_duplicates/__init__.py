from basic_data_structures.linked_list import Node


def solution(head):
    """
    Deletes duplicate values from a sorted linked list.


    Complexity: O(n) where `n` is the size of an input list
    :param Node head: Head of an input list
    :return Node: Head of updated list
    """
    node = head
    while node:
        # Fast-forward to next unique key
        while node.next and node.next.key == node.key:
            node.next = node.next.next
        node = node.next
    return head
