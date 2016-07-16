def backtrack(S, T, i=None, j=None):
    """
    Edit distance solver using recursion.

    In computer science, edit distance is a way of quantifying how dissimilar two strings
     are to one another by counting the minimum number of operations required to transform
     one string into the other.

    Complexity: O(3^n), a very inefficient algorithm
    :param str S: Source string
    :param str T: Target string
    :param int i: Pointer index in `S` (used in recursion)
    :param int j: Pointer index in `T` (used in recursion)
    :return int: Edit distance between `S` and `T`
    """
    if i is None or j is None:  # Initializing pointers
        i = len(S)
        j = len(T)
    if i == 0:
        return j * cost_insert(T[j - 1])
    if j == 0:
        return i * cost_delete(S[i - 1])
    a, b = S[i - 1], T[j - 1]  # Pick next two characters to compare
    return min(
        backtrack(S, T, i - 1, j - 1) + cost_replace(a, b),
        backtrack(S, T, i, j - 1) + cost_insert(b),
        backtrack(S, T, i - 1, j) + cost_delete(a)
    )


def cost_replace(x, y):
    """
    Returns the cost of replacement of two characters in a string.

    Complexity: O(1)
    :param str x: First character
    :param str y: Second character
    :return int: Cost of replacement
    """
    if x == y:
        return 0
    else:
        return 1


def cost_insert(x):
    """
    Returns the cost of insertion of an arbitrary character into a string.

    Complexity: O(1)
    :param str x: Subject character
    :return int: Cost of insertion
    """
    return 1


def cost_delete(x):
    """
    Returns the cost of deletion of an arbitrary character from a string.

    Complexity: O(1)
    :param str x: Subject character
    :return int: Cost of deletion
    """
    return 1


print(backtrack("bob", "mob"))
