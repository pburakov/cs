from abstract_data_types.linked_list import UnorderedList


def sequential_search(list, needle):
    """
    Brute force iteration search. For explanation, see linked list search.
     Note: average and worst case is faster for an Ordered list.
    """
    linked_list = UnorderedList()
    for i in list:
        linked_list.add(i)
    return linked_list.search(needle)


def binary_search(ordered_list, needle):
    """
    Divide-and-conquer search algorithm, works ONLY for ordered lists. It is very
     similar to a Binary Tree Search. Determines in which part of the list
     Needle is located by checking midpoint value and gradually reducing the
     search window by moving Left and Right marker indexes.
    """
    left = 0
    right = len(ordered_list) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if ordered_list[midpoint] == needle:
            return True
        else:
            if needle < ordered_list[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return False


def binary_rec_search(ordered_list, needle):
    """
    Recursive version of a Binary Search. List is being split to smaller pieces
     and each chunk is then recursively searched based on anticipated item index.
    """
    if len(ordered_list) == 0:
        return False
    else:
        midpoint = len(ordered_list) // 2
        if ordered_list[midpoint] == needle:
            return True
        else:
            if needle < ordered_list[midpoint]:
                return binary_rec_search(ordered_list[:midpoint], needle)
            else:
                return binary_rec_search(ordered_list[midpoint + 1:], needle)
