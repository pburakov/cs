from basic_data_structures.linked_list import LinkedList, Node


def find(L):
    """
    Detects beginning of a cycle in a linked list.

    Once the cycle is detected (using two list runners method).

    Complexity: O(n), no extra space
    :param LinkedList L: Input linked list
    :return Optional[Node]: Pointer to a first node in a cycle.
    """
    p1 = p2 = L.head
    has_loop = False
    while p1 and p2 and p1.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 is p2:
            has_loop = True
            break
    if has_loop is True:
        p1 = L.head
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next
        return p2
    else:
        return None
