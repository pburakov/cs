"""
Combinatorial Search
====================

Many combinatorial search problems can be solved to optimality using exhaustive search
techniques, although computational cost of such solutions can be enormous, even unfeasible.
Time and space complexity of such problems are coherent with the size of their output.

This type of problems is often called **"n-choose-k"**, due to the binomial coefficient,
often used in combinatorics. Binomial coefficient denotes the number of
:math:`k`-permutations of an :math:`n`-set. It is usually written as
:math:`{n\\choose k} = C(n,k) = \\frac{n!}{k!(n-k)!}`.

Combinatorial search algorithms without optimization use recursion with a **backtracking**
technique. Recursive solutions resemble a depth-first search algorithm where the graph
represents all possible configurations, or states. Backtracking is a systematic way to
iterate through all the sates in a search space, while avoiding repetitions and bad
configurations. Backtracking algorithm abandons a configuration branch as soon as it
determines that it cannot possibly lead to a valid solution

Description of common steps of a backtracking algorithm:

 - Define one or many base cases for recursion to finish. For instance, report a found
   solution or report that algorithm has exhausted all possible solutions, or reached an
   and end while iterating through a given configuration.
 - Construct a new solution candidate, or several. For example, exclude, swap or replace
   an element of a set.
 - Check if a proposed candidate does not violate problem conditions. This is where we
   abandon a branch of a recursive tree.
 - Call itself on a new candidate or, if there are many, on each of the new candidates.
 - Undo the updates made to a configuration (optional). This step occurs after the running
   process exits the recursion (or "backtracks").

This module contains implementation templates and techniques for some of the most common
combinatorial search problems.
"""


def permutations(S, T, i=0):
    """Produces all permutations of a set.

    Permutation of a set contains all the same elements, but in a different order. For
    example, :math:`\{B, A, C\}` and :math:`\{B, C, A\}` are valid permutations of the set
    :math:`\{A, B, C\}`.

    This algorithm exhaustively searches all possible combinations of elements in a set
    by continuously swapping pairs of elements using recursion, then backtracks to
    the original state of a set.

    Complexity:
        :math:`\Theta (n!)`. There are :math:`n!` permutations of a set of :math:`n`
        elements.

    :param list S: Input set.
    :param list T: Target list of set permutations.
    :param int i: Starting index (used in recursion).

    """
    n = len(S)
    if i >= n:
        T.append(S.copy())
    else:
        for k in range(i, n):
            S[i], S[k] = S[k], S[i]  # Swap
            permutations(S, T, i + 1)  # Backtrack
            S[i], S[k] = S[k], S[i]  # Swap back


def subsets(S, T, i=0, s=None):
    """Produces all subsets of a set.

    Exhaustively searches all possible subsets of a set (Python list). Order is not
    important. For example, :math:`\{1, 3\}` and :math:`\{3, 1\}` are the same subset.

    At each step, the algorithm "decides" whether to include next element or not. Same
    algorithm is invoked for each decision. The problem is solved in the same manner as a
    permutation problem.

    Complexity:
        :math:`\Theta (2^n)` corresponds with a binary recursive tree, and a number of
        possible ways to choose :math:`k` element out of the :math:`n` positions.

    :param list S: Input set.
    :param list T: Target powerset.
    :param int i: Element lookup index (used in recursion).
    :param list s: Intermediate subset (used in recursion).

    """
    if s is None:
        s = []  # Subset stack
    n = len(S)
    if i >= n:
        if len(s) > 0:
            T.append(s.copy())
    else:
        s.append(S[i])
        subsets(S, T, i + 1, s)  # Generate subsets including `i`-th element
        s.pop()
        subsets(S, T, i + 1, s)  # Generate subsets excluding `i`-th element


def partitions(S, T, i=0, p=None):
    """Produces partitions of a set, preserving the order of elements.

    Partitioned set contains such subsets that, when joined, produce the original
    set. Order of elements is preserved. For example a set :math:`\{a,b,c\}` can be
    partitioned into :math:`\{a,b,c\}`, :math:`\{a\}+\{b,c\}`, :math:`\{a,b\}+\{c\}` or
    :math:`\{a\}+\{b\}+\{c\}`.

    This algorithm is similar to subsets generation. Instead of deciding whether to
    include an element into a partition, it decides whether the set should be "sliced" at
    this point, starting at the beginning of the set. The remainder sub-partition to the
    "right" of the slice, is added to the stack and the same algorithm is called on it.

    After sub-partitions have been computed, the algorithm "backtracks" and pops counted
    elements of the partition from the stack. Then operation is repeated.

    Complexity:
        :math:`O(2^n)`, more tightly bound by :math:`^{2^n}/_2` possible partitions.

    :param list S: Input set.
    :param list T: Target list of set partitions.
    :param int k: Starting index (used in recursion).
    :param list p: Intermediate partition stack (used in recursion).

    """
    if p is None:
        p = []  # Partition stack
    n = len(S)
    if i >= n:
        T.append(p.copy())
    else:
        for k in range(i + 1, n + 1):
            sub_partition = S[i:k]
            p.append(sub_partition)
            partitions(S, T, k, p)
            p.pop()
