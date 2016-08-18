"""
 [ - - - - - - - - -]
   1---3       7---9
   1-------5
     2---4
       3-----6

"""


def solution(L):
    """
    Returns list of merged intervals.

    Complexity: O(n log(n)), array is sorted using Python's timsort
    :param list[tuple]] L: Non-empty list of intervals
    :return list[tuple]: List of merged intervals
    """
    out = []
    X = sorted(L)
    x, y = X[0]
    for a, b in X:
        if a <= y:
            y = max(b, y)
        else:
            out.append((x, y))
            x = a
            y = b
    out.append((x, y))
    return out
