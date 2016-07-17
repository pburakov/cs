"""
Nuts and Bolts problem is also known as Lock and Key or Red and Blue Water Jugs problem.
 The task is to sort values in two arrays `N` and `B` with one constraint. The values
 from the same array cannot be compared. Value from array `N` can only be compared to a
 value in array `B`. Arrays are of the same length and contain same elements but in
 different order. Sort arrays `N` and `B` in place.
"""


def solution(N, B):
    """
    Nuts and Bolts problem solver.

    Arrays may consist of any comparable objects: chars, strings, ints or floats.

    :param list[object] N: List of nuts
    :param list[object] B: List of bolts
    :return None: `N` and `B` are sorted
    """
    r = len(B) - 1
    nb_quicksort(N, B, 0, r)


"""
Auxiliary routines used in the solution
"""


def nb_quicksort(N, B, q=0, r=-1):
    """
    Modified quicksort algorithm that solves Nuts and Bolts problem.

    This is basically a quicksort algorithm with modified partitioning scheme that takes
     an arbitrary pivot value and finds a match in the array, just like finding a single
     matching "bolt" to a "nut".

    Complexity: O(n log(n)), implementation of quick sort algorithm.
    :param list[object] N: List of nuts
    :param list[object] B: List of bolts
    :param int q: Lower bound of sorting (default is 0)
    :param int r: Upper bound of sorting (default is |B|-1)
    :return None: `N` and `B` are sorted
    """
    if q < r:
        p = partition(N, B[r], q, r)
        partition(B, N[p], q, r)
        nb_quicksort(N, B, q, p - 1)
        nb_quicksort(N, B, p + 1, r)


def partition(S, x, q, r):
    """
    Hoare partition scheme against arbitrary pivot value.

    Swaps elements that a smaller than value `x` to the left side of the list and places
     matching pivot element on its final position.

    :param list[object] S: Input array
    :param object x: Pivot value
    :param int q: Lower bound
    :param int r: Upper bound
    :return int: Index of a final position of a pivot value
    """
    i, j = q, q
    while j < r:
        if S[j] < x:
            S[i], S[j] = S[j], S[i]
            i += 1  # Stops increasing after last encountered smaller element
        elif S[j] == x:
            S[j], S[r] = S[r], S[j]
            j -= 1
        j += 1
    S[i], S[r] = S[r], S[i]
    return i
