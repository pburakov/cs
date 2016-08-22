"""
"""


def manacher(S):
    """
    Returns longest palindromic substring

    It converts
    ```
    banana -> | b | a | n | a | n | a |
              0 1 0 1 0 3 0 5 0 3 0 1 0
    ```

    :param str S:
    :return:
    """
    # Building augmented string for processing
    P = ['|']
    for c in S:
        P.append(c)
        P.append('|')
    n = len(P)
    M = [0] * n  # Map of palindrome lengths
    M[1] = 1  # Second element is a single-letter palindrome
    s, e = 1, 2
    return S[s:e]


def expand(S, M, k):
    """
    Returns length of a palindrome with center at given index.

    Complexity: O(n)
    :param list[str] S: List or processed string characters
    :param list[int] M: Map with the count of longest palindrome
    :param int k: Center index
    :return int: Length of max palindrome with center at index `k`
    """
    if S[k] == '|':
        count = 0
    else:
        count = 1
    n = len(S)
    o = 1  # Window offset
    while 0 <= k - o and k + o < n:
        a = S[k - o]
        b = S[k + o]
        if a == b:
            count += M[k - o] + M[k + o]
        else:
            break
        o += 1
    return count


print(manacher("banana"))
