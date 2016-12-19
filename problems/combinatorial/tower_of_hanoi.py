"""
Tower of Hanoi
==============

Tower of Hanoi is a classic problem that is often used to demonstrate recursion. Exact conditions are described `here`_

.. _here: https://en.wikipedia.org/wiki/Tower_of_Hanoi

Solution algorithm for two disks is simple. Let :math:`A` be the original pole, :math:`B`
the destination and :math:`C` the auxiliary pole. Problem can be solved in following steps:

    1. pick from :math:`A`, put on :math:`C`;
    2. pick another disk from :math:`A`, put directly onto :math:`B`;
    3. pick disk from :math:`C`, put on :math:`B`.

"""


def move_tower(A, B, C, h=None):
    """Recursive Tower of Hanoi solver that prints out the state after each move.

    We already have a solution for two disks (height :math:`h=2`). However, if we add
    another disk into the problem (:math:`h=3`), we're going to need to generalize the
    approach.

    First we need to solve Tower of Hanoi problem for poles :math:`A` and :math:`C` and
    :math:`h-1` (or first three disks), which is recursive step 1. We're going to need to
    use pole :math:`B` as an auxiliary.

    Then we move the last remaining disk from :math:`A` to :math:`B` (step 2). After that
    we solve Tower of Hanoi for remaining disks or :math:`h-1-1` for poles :math:`C` and
    :math:`B`, this time using pole :math:`A` as an auxiliary (recursive step 3).

    :math:`h=1` becomes our base case when we halt the recursion and proceed to the next
    step, which denotes that we also need to keep track of the height of the tower.

    Complexity:
        :math:`O(2^n)`. The time and space complexity is bounded by the number of moves,
        which grows exponentially with every added disk.

    :param list[str] A: Origin pole.
    :param list[str] B: Target pole.
    :param list[str] C: Auxiliary pole.

    """
    if h is None:
        h = len(A)
    if h > 0:
        move_tower(A, C, B, h - 1)
        print(A, B, C)
        move_disk(A, B)
        print(A, B, C)
        move_tower(C, B, A, h - 1)


def move_disk(P1, P2):
    """Moves disk from pole 1 to pole 2, represented as a list.

    Complexity:
        :math:`O(1)`.

    :param list[str] P1: Mutable pole 1 (origin).
    :param list[str] P2: Mutable pole 2 (target).
    """
    P2.append(P1.pop())
