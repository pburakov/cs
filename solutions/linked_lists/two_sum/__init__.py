def solution(L, s):
    """
    Two sum solver.

    Brute force solution would scan the list repeatedly to find a pair for every element
     in it, which would give us O(n^2) running time, but we can do better if we use some
     extra space for a hash table with O(1) lookup.

    The solution is simple. Construct a frequency map for every encountered element. Then
     traverse the list again and check if a pair that adds up to a target sum is present
     in the frequency map.

    Complexity: O(n) time, O(n) space
    :param List L: Input list
    :param int s: Target sum
    :return bool: Returns True if list contains the target sum, False otherwise
    """
    freq_map = {}
    # First run (populate the frequency map)
    node = L.head
    while node:
        if node.key not in freq_map:
            freq_map[node.key] = 0
        freq_map[node.key] += 1
        node = node.next
    # Second run (lookup for a pair)
    node = L.head
    while node:
        freq_map[node.key] -= 1
        remainder = s - node.key
        if remainder in freq_map and freq_map[remainder] > 0:
            return True
        freq_map[node.key] += 1
        node = node.next
    return False


"""
Auxiliary data structures used in the solution
"""


class Node:
    def __init__(self, key):
        """
        Node of a singly linked list containing arbitrary pointer.

        :param object key: Node key
        """
        self.key = key
        self.next = None

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

        Complexity: O(1)
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
            out += " -> "
            node = node.next
        out += "null"
        return out
