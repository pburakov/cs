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
