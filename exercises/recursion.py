"""
Taken from "Cracking the Coding Interview" book by GayleMcDowell, 2015.

A child is running up a staircase with n steps and can hop either 1 step, 2 steps,
 or 3 steps at a time. Implement a method to count how many possible ways the child
 can run up the stairs.
"""

from algorithms.memoization import memoize


@memoize
def count_ways(n):
    """
    This is a classic "top-down" solution.
    What would be a child last move before reaching a top stair? Child either hopped
     there from a previous step, or 2 or 3 step away. So the final number will be
     the sum of all the possible ways to get there form beyond all of those.

    Please note 1 for n == 0 as reaching top of the stairs counts as a move.

    The complexity of this algorithm is O(3^n) without memoization.

    @:param n: number of stairs
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)


print("\n-- Hopping the stairs --")
print(count_ways(1))
print(count_ways(2))
print(count_ways(3))
print(count_ways(5))
print(count_ways(7))
print(count_ways(25))


def move_tower(h, from_pole, to_pole, with_pole):
    """
    This is a simple recursive solution for Tower Of Hanoi puzzle.
     More info: https://en.wikipedia.org/wiki/Tower_of_Hanoi

    Initiates a recursive Tower Of Hanoi algorithm to move h disks between
     first two poles via the third pole. The tree of required actions is printed
     to the console.
    Caution: number of actions grows exponentially for each step of h. Use of larger
     h values may overwhelm the output.

    :param h: Height of the original (ordered) pyramid
    """
    if h >= 1:
        move_tower(h - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(h - 1, with_pole, to_pole, from_pole)


def move_disk(fp, tp):
    """
    Prints the moving action.
    """
    print("moving disk from", fp, "to", tp)


print("\n-- Tower of Hanoi --")
move_tower(3, "A", "B", "C")
