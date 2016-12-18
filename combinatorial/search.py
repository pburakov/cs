"""
Combinatorial Search
====================

Many combinatorial search problems can be solved to optimality using exhaustive search
techniques, although computational cost of such solutions can be enormous, even unfeasible.
Time and space complexity of such problems are coherent with the size of its output. It
can be predicted using counting theory formulas for **exhaustive search**.

This type of problems is often called **"n-choose-k"**, due to the binomial coefficient
that denotes the number of :math:`k`-combinations of a set of :math:`n` elements.

Combinatorial search algorithms use recursion with a **backtracking** technique. Recursive
solutions resemble depth-first search algorithm where graph represents all possible
configurations, or states. Backtracking is a systematic way to iterate through all the
sates in a search space, while avoiding repetitions and bad configurations. Backtracking
algorithm abandons a partial candidate as soon as it determines that it cannot possibly
lead to a valid solution

Description of common steps of a backtracking algorithm:

 - Define base case for recursion to finish. For instance, report a found solution or
   report that algorithm has exhausted all possible solutions for given configuration.
 - Construct a new solution candidate, or several. For example, exclude, swap or replace
   an element of a set.
 - Check if proposed solution does not violate problem conditions. This is where we
   abandon a branch of a recursive tree (not shown in examples).
 - Call itself on new candidate or, if there are many, on each of the new candidates.
 - Undo updates made to a set (optional). This step occurs after the running process
   exits the recursion (or "backtracks").

This module contains implementation templates and techniques for some of the most common
combinatorial search problems.
"""


def subsets(S, P, i=0, M=None):
    """Produces all subsets of a set.

    Exhaustively searches all possible subsets of a set (Python list). Order is not
    important. For example, :math:`\{1, 3\}` and :math:`\{3, 1\}` are the same subset.

    At each step algorithm "decides" whether to include next element or not. Same
    algorithm is invoked for each decision. The problem is solved in the same manner as a
    permutation problem.

    In this implementation the decisions table is represented as an :math:`n`-sized bit
    map, where bits ``1`` and ``0`` at :math:`i`-th position determine whether :math:`i`-th
    element should be included or not.

    Complexity:
        :math:`\Theta (2^n)` for time. Recursive tree is binary, for each of :math:`n`
        elements we decide whether we include that element in a subset or not.

    :param list S: Input set.
    :param list P: Output list of subsets.
    :param int i: Element lookup index (used in recursion).
    :param list M: Bitmap of a subset (used in recursion).

    """
    n = len(S)
    if M is None:
        M = [False] * n  # Allocating memory for bitmap or a subset
    if i >= n:
        # Converts bit map to a subset copy
        s = [S[i] for i in range(n) if M[i] is True]
        P.append(s)
    else:
        M[i] = True
        subsets(S, P, i + 1, M)  # Generate subsets including `i`-th element
        M[i] = False
        subsets(S, P, i + 1, M)  # Generate subsets excluding `i`-th element


def permutations(S, P, i=0):
    """Produces all permutations of a set.

    Permutation of a set contains all the same elements, but in a different order. This
    algorithm exhaustively searches all possible combinations of elements in a set (Python
    list) by continuously swapping pairs of elements using recursion, then backtracks to
    the original state of a set.

    Complexity:
        :math:`\Theta (n!n)` time. Space complexity is :math:`O(n!n)` is proportional to
        the output. There are :math:`n!` permutations of a set of :math:`n`-elements set
        by definition.

    :param list S: Input set.
    :param list P: Output list of permutations.
    :param int i: Starting index (used in recursion).

    """
    n = len(S)
    if i >= n - 1:
        P.append(S.copy())
    else:
        for k in range(i, n):
            S[i], S[k] = S[k], S[i]  # Swap
            permutations(S, P, i + 1)  # Backtrack
            S[i], S[k] = S[k], S[i]  # Swap back


def partitions(S, P, s=0, p=None):
    """Produces all possible partitions of a set.

    Partitioned set contains such subsets that, when joined, they produce the original
    set. Order of elements is preserved. For example a set :math:`\{a,b,c\}` can be
    partitioned into :math:`\{a,b,c\}`, :math:`\{a\}+\{b,c\}`, :math:`\{a,b\}+\{c\}` or
    :math:`\{a\}+\{b\}+\{c\}`.

    This algorithm is similar to subsets generation. Instead of deciding whether to
    include an element into a partition, it decides whether the set should be "sliced" at
    this point, starting at the beginning of the set. The remainder sub-partition to the
    "right" of the slice, is added to the stack and same algorithm is called on it.

    After sub-partitions have been computed, the algorithm "backtracks" and pops counted
    elements of the partition from the stack. Then operation is repeated.

    Complexity:
        :math:`O(2^n)` bounded by :math:`^{2^n}/_2` possible partitions.

    :param list S: Input set.
    :param list P: Output list of set partitions.
    :param int s: Starting index (used in recursion).
    :param list p: Intermediate partition stack (used in recursion).

    """
    n = len(S)
    if p is None:
        p = []  # Partition stack
    if s >= n:
        P.append(p.copy())
    else:
        for i in range(s + 1, n + 1):
            sub_partition = S[s:i]
            p.append(sub_partition)
            partitions(S, P, i, p)
            p.pop()
