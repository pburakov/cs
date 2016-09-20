from basic_data_structures.linked_list import LinkedList, Node


def find(L):
    """
    Detects beginning of a cycle in a linked list.

    When the cycle is detected (using two list runners), we observe that the meeting
     point is somewhere inside the cycle. If we shift one of the pointers back to the
     head of the list and move them again, one step at a time, the two pointers will meet
     exactly at the desired node.

    Complexity: O(n), no extra space
    :param LinkedList L: Input linked list
    :return Optional[Node]: Pointer to a first node in a cycle.
    """
    p1 = p2 = L.head
    has_loop = False
    while p1 and p2 and p1.next:
        p1 = p1.next  # One step ahead
        p2 = p2.next.next  # Two steps at a time
        if p1 is p2:
            has_loop = True
            break
    if has_loop is True:
        p1 = L.head
        while p1 is not p2:
            p1 = p1.next  # One step ahead
            p2 = p2.next  # One step ahead as well
        return p2
    else:
        return None
