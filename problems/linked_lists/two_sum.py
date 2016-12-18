"""
# Sum of Two Elements

Given a singly linked list with integer elements, find if it has two elements that add up
 to a given sum *s*.

Example:
```
Input: [1 -> 2 -> 3 -> 4], s=5. Output: True
Input: [1 -> 2 -> 3], s=2. Output: False
Input: [1 -> 2 -> 3 -> 1 -> 6], s=2. Output: True
```
"""
from basic.linked_list import LinkedList as List


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
