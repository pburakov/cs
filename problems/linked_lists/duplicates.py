"""
# Remove Duplicates from Sorted Linked List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given `1->1->2`, return `1->2`.
Given `1->1->2->3->3`, return `1->2->3`.
"""
from basic.linked_list import Node


def solution(head):
    """
    Deletes duplicate values from a sorted linked list.

    Algorithm is very straightforward. Instead of keeping track of the values and edge
     cases, we can take advantage from the fact that the list is sorted. We simply
     "fast-forward" the next pointer to the next element that has a different key.

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
