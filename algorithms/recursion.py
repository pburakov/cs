def all_n(n):
    """
    Returns all integer numbers in a range {1..n} as a string.

    Example: n=3, output: "1 2 3"
    :param int n: Integer number
    :return str: Output string
    """
    if n == 1:
        return "1"
    else:
        return str(all_n(n - 1)) + " " + str(n)


def all_range_n(a, b):
    """
    Returns integer range {a..b} in ascending or descending order as a string

    Will return {a..b} if b > a, {b..a} if a > b.

    Example: a=2, b=5, output: "2 3 4 5"
    :param int a: Left bound
    :param int b: Right bound
    :return str: Output string
    """
    if a == b:
        return str(a)
    elif b > a:
        return str(all_range_n(a, b - 1)) + " " + str(b)
    elif b < a:
        return str(a) + " " + str(all_range_n(a - 1, b))


def ackermann(m, n):
    """
    Recursive representation of Ackermann function

    See https://en.wikipedia.org/wiki/Ackermann_function.

    :param int m: First argument
    :param int n: Second argument
    :return int: Output
    """
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def is_prime_pow2(x):
    """
    Evaluates if positive integer is a prime power of two

    Returns True if integer is a prime power of 2, False otherwise

    :param int x: Input integer `x ≥ 1`
    :return bool: Evaluation result
    """
    if x < 1:
        raise ValueError("Expected positive integer number")
    if x == 2:
        return True
    elif 1 <= x < 2:
        return False
    return is_prime_pow2(x / 2)


def digit_sum(x):
    """
    Sum of all digits in an integer number

    Example: x=123, output: 6
    :param int x: Input integer
    :return int: Sum of all digits in `x`
    """
    if x < 1:
        return 0
    elif x < 10:
        return x
    else:
        return x % 10 + digit_sum(int(x / 10))


def permutations(L, P, i=0):
    """
    Produces all permutations of a set

    :param list L: Input set
    :param list P: Output list of permutations
    :param int i: Starting index (optional)
    :return None: List `P` is populated
    """
    n = len(L)
    if i == n - 1:
        P.append(L.copy())
        return
    else:
        for k in range(i, n):
            L[i], L[k] = L[k], L[i]
            permutations(L, P, i + 1)
            L[i], L[k] = L[k], L[i]


def subsets(L, P, r=0, w=0, S=None):
    """
    Produces all subsets of a set

    :param list L: Input set
    :param list P: Output list of subsets
    :param int r: Read index (optional) in input set `L`
    :param int w: Write index (optional) in generated subset `S`
    :param list S: Generated subset (optional)
    :return None: List `P` is populated
    """
    n = len(L)
    if S is None:
        S = [None] * n
    if r >= n:
        P.append(S.copy()[0:w])
        return
    else:
        subsets(L, P, r + 1, w, S)
        S[w] = L[r]
        subsets(L, P, r + 1, w + 1, S)
