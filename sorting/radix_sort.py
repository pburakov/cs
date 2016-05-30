def radix_sort(A, d, b=10):
    """
    Sorts an array of integer elements using radix sort and returns sorted array.

    Radix sort is the algorithm used by the old card-sorting machines. In typical
     computer, radix sort is sometimes used to sort records of information that are keyed
     by multiple fields. For instance, dates, represented by year, month and day.

    Counterintuitively, radix sort sorts by least significant digit first. The process
     is repeated towards most significant digit until entire array is sorted. In order
     for radix sort to work correctly digit sorts must be stable. This implementation
     uses an adapted implementation of counting sort.

    Complexity: O(d(n+k)) given an array of `n` `d`-digit numbers. This is a stable
     algorithm. This implementation requires additional O(n+k) storage for a counting
     sort subroutine and additional O(n) for the output array.
    :param list A: Array to sort
    :param int d: Maximum number of digits for elements in array. Using out-of-bounds
     `d` will result in unnecessary iterations of sorting subroutine.
    :param int b: Base of integer elements in the array (default base is 10)
    :return list: Sorted product of array `A`
    """
    P = A  # Product of sorting iterations
    for i in range(0, d):
        # Stable sort to sort array on digit `i`
        P = digit_counting_sort(P, i, b)
    return P


def digit_counting_sort(A, i, b=10):
    """
    Stable linear-time sort of an array on a single digit.

    This is an adapted implementation of counting sort which sorts elements of an entire
     array based on a single digit. Differences between regular counting sort are
     highlighted with inline comments.

    Complexity: O(n+b), where `n` is the number of elements in array. This is a stable
     sorting algorithm, storage requirements are O(n+b).
    :param list A: Input array
    :param int i: Digit to sort on (reversed). `i=0` being the least significant digit.
    :param int b: Base of integers in array `A`. Base here serves as an upper bound `k` for
     digits involved in sorting. Default base is 10.
    :return list: Sorted product of array `A`
    """
    n = len(A)
    i_n = n - 1     # Index of a last element in the input array
    P = [None] * n  # Allocated memory for sorted output
    R = [0] * b     # Working storage for all possible numbers in radix representation

    for e in A:
        d = get_digit(e, i, b)  # `i`-th digit of an element `e`
        R[d] += 1
    # `R[d]` now contains number (count) of elements having `i`-th digit equal to `d`
    for d in range(1, b):
        R[d] += R[d - 1]
    # `R[d]` now contains the number of elements having `i`-th digit that is less
    # than or equal to `d`.

    # Iterating backwards to maintain stability, same as regular counting sort
    for j in range(i_n, -1, -1):
        e = A[j]                # Element in input array
        d = get_digit(e, i, b)  # `i`-th digit of an element `e`
        # Let `k` be the location index of element `e` in the output array sorted on `i`-th
        # digit `d`. Deducting `1` since indexes are zero-based, but the counts are not.
        k = R[d] - 1
        P[k] = e
        # Counter is updated in order to keep the next element with the same `i`-th digit
        # in its value from overwriting previous one.
        R[d] -= 1
    return P


def get_digit(n, i, b=10):
    """
    Returns given digit of an integer in arbitrary base representation.
    :param int n: Input integer
    :param int i: Digit to return (reversed). `i=0` being the least significant digit.
     Using out-of-bounds `i` will produce trailing 0.
    :param int b: Base of `n` (default base is 10)
    :return int: `i`-th digit of an input integer or trailing 0
    """
    return (n // b ** i) % b
