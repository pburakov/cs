"""
Linear Sorting Algorithms
=========================

Linear sorting algorithms such as counting sort, radix sort and bucket sort break the
lower bound of comparison sort. In fact, for each of these algorithms, no comparisons
between input elements occur in the code.
"""


def counting_sort(A, k):
    """Sorts an array of integers using counting sort and returns a sorted array.

    Counting sort assumes that each element in the array is an integer within the range
    :math:`[0..k]`. The algorithm determines, for each element :math:`x`, the number of
    elements less than :math:`x`. It uses this information to place an element :math:`x`
    onto its position in the output array.

    Counting sort is a stable sorting algorithm. Stability is not important for sorting
    arrays of integers without any satellite data carried with them, but it is critical,
    when the counting sort is used as a subroutine of a radix sort.

    Complexity:
        :math:`O(n+k)`, where :math:`k` is the number of distinct elements in the array.
        Counting sort requires additional :math:`n`-sized storage for the output and an
        auxiliary storage of size :math:`k`.

    :param list[int] A: Array to sort.
    :param int k: Inclusive upper bound for the range of integers in the array. For
     example, for :math:`A = \{ 0, 1, 3 \}`, :math:`k = 3` or :math:`max(A)`.
    :return: Sorted array.

    """
    n = len(A)
    i_n = n - 1  # Index of last element
    P = [int] * n  # Allocated memory for sorted output
    C = [0] * (k + 1)  # Working storage (auxiliary array for counting)
    for x in A:
        C[x] += 1
    # `C[x]` now contains number (count) of elements equal to `x`
    for x in range(1, k + 1):
        C[x] += C[x - 1]
    # `C[x]` now contains number of elements less than or equal to `x`.
    # Array `C` serves as an initial index map for the final location of each element
    # in the sorted output. We need to go backwards to preserve stability of the sort.
    for j in range(i_n, -1, -1):
        e = A[j]
        # Let `i` be the location index of element `e` in the output array. Deducting `1`,
        # since indexes are zero-based, but the counts are not.
        i = C[e] - 1
        P[i] = e
        # Counter is updated in order to keep the next element with the same value from
        # overwriting a previous one.
        C[e] -= 1
    return P


def bucket_sort(A):
    """Sorts an array of integers using bucket sort algorithm and returns a sorted array.

    Bucket sort is fast because it makes assumptions about the input. It is efficient
    when the input is drawn from a uniform distribution. Evenly distributed items can be
    sorted into individual buckets and then drawn back in order. Depending on the nature
    of the input, additional sorting routines may be performed on each bucket.

    Bucket sort is stable if buckets maintain LIFO properties.

    Complexity:
        :math:`O(n+k)` in average case for uniformly or evenly distributed input, where
        :math:`k` is the number of "buckets". Worst case :math:`O(n^2)`.

    :param list[int] A: Input array.
    :return: Sorted array.

    """
    n = len(A)
    P = [int] * n  # Allocated memory for the sorted output
    B = [None] * n  # Array of buckets
    for i in A:
        if B[i] is None:
            B[i] = []
        B[i].append(i)
    i = n - 1
    for j in range(n - 1, -1, -1):  # Going backwards to maintain stability
        while B[j]:
            P[i] = B[j].pop()
            i -= 1
    return P


def radix_sort(A, d, b=10):
    """Sorts an array of integer elements using radix sort and returns a sorted array.

    Radix sort is the algorithm used by the old card-sorting machines. In a typical
    computer, radix sort is sometimes used to sort records of information that are keyed
    by multiple fields. For instance, dates, represented by year, month and day.

    Counterintuitively, radix sort sorts by least significant digit first. The process is
    repeated towards the most significant digit until the entire array is sorted. In order
    for radix sort to work correctly, the sorting of digits must be stable. This
    implementation uses an adapted implementation of counting sort.

    Complexity:
        :math:`O(d(n+k))` given an array of :math:`n` :math:`d`-digit numbers. Radix sort
        is a stable sorting algorithm. This implementation requires additional
        :math:`O(n+k)` storage for a counting sort subroutine and additional :math:`O(n)`
        for the output array.

    :param list[int] A: Array to sort.
    :param int d: Maximum number of digits for all elements found in an array. Using
     greater :math:`d` will result in unnecessary iterations of the sorting subroutine.
    :param int b: Base of integer elements in the array (default base is 10).
    :return: Sorted array.

    """
    P = A.copy()
    for i in range(0, d):
        # Stable sort to sort array on digit `i`
        P = digit_counting_sort(P, i, b)
    return P


"""
Subroutines used in Radix Sort
"""


def digit_counting_sort(A, i, b=10):
    """Stable linear-time sorting algorithm of an array based on a single digit.

    This is an adapted implementation of counting sort which sorts elements of an entire
    array based on a single digit. Differences between regular counting sort are
    highlighted in inline comments.

    This is a stable sorting algorithm.

    Complexity:
        :math:`O(n+b)`, where :math:`n` is the number of elements in array. Storage
        requirements are :math:`O(n+b)`.

    :param list[int] A: Input array.
    :param int i: Digit to sort on, :math:`i=0` being the least significant digit.
    :param int b: Base of integers in the input array. Base here serves as an upper bound
     :math:`k` for digits involved in sorting. Default base is 10.
    :return: Sorted array.

    """
    n = len(A)
    i_n = n - 1  # Index of a last element in the input array
    P = [int] * n  # Allocated memory for sorted output
    R = [0] * b  # Working storage for all possible numbers in radix representation
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
        e = A[j]  # Element in input array
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
    """Returns i-th digit of an integer in an arbitrary base representation.

    :param int n: Input integer.
    :param int i: Digit to return, :math:`i=0` being the least significant digit. Using
     greater :math:`i` will produce trailing zeroes.
    :param int b: Base of :math:`n`. Default base is 10.
    :return: :math:`i`-th digit of an input integer.

    """
    return (n // b ** i) % b
