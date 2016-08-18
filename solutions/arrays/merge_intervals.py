"""
Given a list of tuples, where each tuple is two integers `(start, end)`, merge
 overlapping intervals:
    ```
     [ - - - - - - - - -]
       1---3       7---9
       1-------5
         2---4
           3-----6
    ```
Input: `[(1, 3), (3, 6), (1, 5), (2, 4), (7, 8)]`
Output: `[(1, 6), (7, 8)]`
"""


def solution(L):
    """
    Returns list of merged intervals.

    Solution is pretty straightforward. Algorithm traverses the array and looks if the
     next interval starts before current one ends. Special care should be taken when
     preparing edge cases for testing.

    Complexity: O(n log(n)), array is sorted using Python's timsort, O(1) space for
     keeping single current interval in memory.
    :param list[tuple]] L: Non-empty list of intervals
    :return list[tuple]: List of merged intervals
    """
    out = []
    X = sorted(L)
    x, y = X[0]
    for a, b in X:
        if a <= y:
            y = max(b, y)  # Extending the interval or keeping the boundary
        else:
            out.append((x, y))
            x = a
            y = b
    out.append((x, y))
    return out
