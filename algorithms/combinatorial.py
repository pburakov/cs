"""
Many combinatorial problems can be solved to optimality using exhaustive search
 techniques, although time complexity of such solutions can be enormous, even
 unfeasible. The time and spaces complexity of a combinatorial search problem is
 coherent with the size of its output. Output is predictable with the use of
 counting theory formulas.

This class of problems is often called "n-choose-k", due to the binomial
 coefficient that denotes the number of `k`-combinations of an `n`-set of
 elements.

Combinatorial search algorithms use recursion with a backtracking technique.
 Backtracking is a systematic way to iterate through all the possible states in
 a search space, while avoiding repetitions and bad configurations. Such solutions
 resemble depth-first search algorithm where graph represents all possible
 configurations.

Description of common steps of a backtracking algorithm:
 1. Define base case for recursion to finish. For instance, report a found solution
  or report that algorithm has exhausted all possible solutions for given
  configuration.
 2. Construct a new candidate configuration for a solution (a state) by updating
  initial set. For example, swap or replace an element or on the contrary, "lock" an
  element and rearrange remaining elements in a set.
 3. Check if proposed solution does not violate conditions, if such are defined by
  the problem. This is where we cut of a branch of a recursive tree.
 4. Backtrack (call the same method) on new candidate or, if many, invoke
  backtracking on each new candidate.
 5. Undo updates made to a set (optional). After the running process will exit the
  recursion set will be returned to an original state.

Below are the implementations of some common combinatorial algorithms that share
 the use of backtracking technique.
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
