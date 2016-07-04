def tower_of_hanoi(P):
    """
    Tower of Hanoi solver.

    Classic recursive problem. Here's a simple solution for two disks:
     Let A be the original rod, B the destination, C auxiliary rod.
     - pick from A, put on C
     - pick another disk from A, put directly onto B
     - pick disk from C, put on B

    However, if we add another disk into the problem, we're going to need to
     generalize the approach.

    First we need to solve Tower of Hanoi problem for rods `A` and `C` for `h-1` or
     3 first disks (recursive step 1) using rod `B` as an auxiliary.

    Then we move the last remaining disk from A to B (step 2).

    After that we solve Tower of Hanoi for remaining disks or `h-1-1` for rods `C`
     and `B`, this time using rod A as an auxiliary (recursive step 3).

    `h=1` becomes our base case when we halt the recursion and proceed to the next
    step.

    :param list[str] P: origin pole
    :return None: Prints the output
    """
    h = len(P)
    move_tower(h, P, [], [])


def move_disk(P1, P2):
    """
    Moves disk from Pole 1 to Pole 2, represented as a list.

    :param list[str] P1: origin pole
    :param list[str] P2: target pole
    :return None: P1 and P2 are updated
    """
    P2.append(P1.pop())


def move_tower(h, A, B, C):
    """
    Recursive Tower of Hanoi solver that prints out the state after each move.

    :param int h: height of pile
    :param list[str] A: origin pole
    :param list[str] B: target pole
    :param list[str] C: auxiliary pole
    :return None: Prints the output. A, B and C are updated.
    """
    if h > 0:
        move_tower(h - 1, A, C, B)
        print(A, B, C)
        move_disk(A, B)
        print(A, B, C)
        move_tower(h - 1, C, B, A)

tower_of_hanoi(list("123"))