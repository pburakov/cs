def find(A):
    """
    Finds majority element in the list.

    Complexity: O(n), no extra space is used
    :param list[object] A: Input list
    :return Optional[object]: Majority element or None if not found
    """
    c = 0  # Candidate index
    count = 1
    n = len(A)
    for i in range(1, n):
        if A[c] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            c = i
            count = 1
    candidate = A[c]
    count = 0
    for a in A:
        if a == candidate:
            count += 1
    if count >= n / 2:
        return candidate
    else:
        return None
