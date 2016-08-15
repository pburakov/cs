"""
Tower of Hanoi is a classic problem that is often used to demonstrate recursion.
 Conditions are described here: [https://en.wikipedia.org/wiki/Tower_of_Hanoi

Solution for two disks is simple. Let `A` be the original rod, `B` the destination and
 `C` the auxiliary rod. Problem can be solved in following steps.
 1. pick from `A`, put on `C`
 2. pick another disk from `A`, put directly onto `B`
 3. pick disk from `C`, put on `B`
"""


def move_tower(A, B, C, h=None):
    """
    Recursive Tower of Hanoi solver that prints out the state after each move.

    We already have a solution for two disks. However, if we add another disk into the
     problem (`h=3`), we're going to need to generalize the approach.

    First we need to solve Tower of Hanoi problem for rods `A` and `C` and `h-1` (or
     first three disks), which is recursive step 1. We're going to need to use rod `B` as
     an auxiliary.

    Then we move the last remaining disk from A to B (step 2). After that we solve Tower
     of Hanoi for remaining disks or `h-1-1` for rods `C` and `B`, this time using rod `A`
     as an auxiliary (recursive step 3).

    `h=1` becomes our base case when we halt the recursion and proceed to the next step,
     which denotes that we also need to keep track of the height of the tower.

    Complexity: O(2^n). The time and space complexity is bounded by the number of moves,
     which grows exponentially with every added disk.
    :param list[str] A: origin pole
    :param list[str] B: target pole
    :param list[str] C: auxiliary pole
    :return None: Prints the output. A, B and C are updated.
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
    """
    Moves disk from Pole 1 to Pole 2, represented as a list.

    Complexity: O(1)
    :param list[str] P1: origin pole
    :param list[str] P2: target pole
    :return None: P1 and P2 are updated
    """
    P2.append(P1.pop())
