def solution(A, B):
    """
    One away linear time problem solver.

    Subroutines are divided for code clarity, but they have common error checking, and
     can be combined.

    Complexity: O(n)
    :param str A: First string
    :param str B: Second string
    :return bool: True if `A` and `B` are one edit away from each other, False otherwise
    """
    if len(A) == len(B):
        return one_replacement_away(A, B)
    elif abs(len(A) - len(B)) < 2:
        return one_insert_away(A, B)
    return False


"""
Auxiliary routines used in the solution
"""


def one_replacement_away(A, B):
    """
    Subroutine, determining if two strings are more than one replacement away.

    Complexity: O(n) where `n` is the length of string, and `A` and `B` are of the same
     length.
    :param str A: First string
    :param str B: Second string
    :return bool: True if `A` and `B` are one replacement away from each other, False
     otherwise.
    """
    errors = 0
    for i in range(0, len(A)):
        if A[i] != B[i]:
            errors += 1  # Accumulate errors
        if errors > 1:
            return False
    return True


def one_insert_away(A, B):
    """
    Subroutine, determining if two strings are more than one insert/delete away.

    Complexity: O(n) where `n` is the length of a smaller string
    :param str A: First string
    :param str B: Second string
    :return bool: True if `A` and `B` are one insert/delete away from each other, False
     otherwise.
    """
    a, b = 0, 0  # Rolling indices
    errors = 0
    while a < len(A) and b < len(B) and errors < 2:
        if A[a] != B[b]:
            errors += 1  # Accumulate errors
            if a + 1 < len(A) and A[a + 1] == B[b]:
                a += 1  # Character is missing in `B`
            elif b + 1 < len(B) and B[b + 1] == A[a]:
                b += 1  # Character is missing in `A`
        else:
            a += 1
            b += 1
    return errors < 2
