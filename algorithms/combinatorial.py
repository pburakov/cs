"""
Many combinatorial problems can be solved to optimality using exhaustive search
 techniques, although computational cost of such solutions can be enormous, even
 unfeasible. The time and spaces complexity of such problems are coherent with the
 size of its output. It is predictable with the use of counting theory formulas.

This class of problems is often called "n-choose-k", due to the binomial
 coefficient that denotes the number of `k`-combinations of a set of `n` elements.

Combinatorial search algorithms use recursion with a backtracking technique.
 Recursive solutions resemble depth-first search algorithm where graph represents all
 possible configurations, or states. Backtracking is a systematic way to iterate
 through all these sates in a search space, while avoiding repetitions and bad
 configurations. Backtracking algorithm abandons a partial candidate as soon as
 it determines that it cannot possibly be completed to a valid solution

Description of common steps of a backtracking algorithm:
 1. Define base case for recursion to finish. For instance, report a found solution
  or report that algorithm has exhausted all possible solutions for given
  configuration.
 2. Construct a new candidate, or several, for a solution. For example, swap or
  replace an element or on the contrary, "lock" an element and rearrange remaining
  elements in a set.
 3. Check if proposed solution does not violate conditions, if such are defined by
  the problem. This is where we abandon a branch of a recursive tree.
 4. Call itself on new candidate or, if many, on each of the new candidates.
 5. Undo updates made to a set (optional). This step occurs after the running process
  exits the recursion (or "backtracks").

Below are the implementations of some common combinatorial search algorithms.
"""


def permutations(L, P, i=0):
    """
    Produces all permutations of a set

    Exhaustively searches all possible combinations of elements in a set (Python list)
     by continuously swapping pairs of elements using recursion with backtracking.

    Complexity: Theta(nn!) time. Space complexity is O(n!n) is proportional to the
     output. There are `n!` permutations of a set of `n`-elements set by definition.
    :param list L: Input set
    :param list P: Output list of permutations
    :param int i: Starting index (used in recursion)
    :return None: List `P` is populated
    """
    n = len(L)
    if i == n - 1:
        P.append(L.copy())  # Creates an exact copy of L
        return
    else:
        for k in range(i, n):
            L[i], L[k] = L[k], L[i]  # Swap
            permutations(L, P, i + 1)
            L[i], L[k] = L[k], L[i]  # Swap back


def subsets(L, P, r=0, w=0, S=None):
    """
    Produces all subsets of a set

    Exhaustively searches all possible subsets of a set (Python list), order is not
     important. For example, `{1, 3}` and `{3, 1}` are the same subset. At each step
     algorithm "decides" whether include next element or not. Same algorithm is called
     for each decision.

    This problem can also be solved as a more space-efficient permutation problem.
     For example we can calculate permutations of `n`-sized bit map, where bits `1` and
     `0` determine whether an element should be included or not.

    Complexity: Theta(2^n) for time. Recursive tree is binary, for each of `n` elements
     we decide whether we include that element in a subset or not.
    :param list L: Input set
    :param list P: Output list of subsets
    :param int r: Read index in input set `L` (used in recursion)
    :param int w: Write index in generated subset `S` (used in recursion)
    :param list S: Intermediately generated subset (used in recursion)
    :return None: List `P` is populated
    """
    n = len(L)
    if S is None:
        S = [None] * n
    if r >= n:
        P.append(S[0:w])  # Creates a sliced copy of S
        return
    else:
        subsets(L, P, r + 1, w, S)  # Subsets without `r`-th element
        S[w] = L[r]  # Add `r`-th element to a candidate
        subsets(L, P, r + 1, w + 1, S)  # Subsets with new candidate


def lcs(X, Y, i=None, j=None):
    """
    Returns longest common sub-sequence of two strings

    This is well known problem whose recursive formula is similar to a subset algorithm.
     Recursion compares two elements at given indices, one for each string, starting at
     the end. Once matching characters are found, one recursive call is made with both
     indices shifted. Otherwise search continues recursively on both strings with one
     index shifted at a time.

    Complexity: O(2^n) for `m=n`, where `m` and `n` are the lengths of the input
     strings.
    :param str X: First string
    :param str Y: Second string
    :param int i: Lookup index in a first string (used in recursion)
    :param int j: Lookup index in a second string (used in recursion)
    :return str: Output string
    """
    if i is None:
        i = len(X) - 1
    if j is None:
        j = len(Y) - 1
    if i < 0 or j < 0:  # Base case (out of bounds)
        return ''
    elif X[i] == Y[j]:  # Matching characters are found
        return lcs(X, Y, i - 1, j - 1) + X[i]
    else:
        # Recursive calls increasing index for each of the string
        s1 = lcs(X, Y, i, j - 1)
        s2 = lcs(X, Y, i - 1, j)
        # Backtrack with the longest string found so far
        if len(s1) > len(s2):
            return s1
        else:
            return s2
