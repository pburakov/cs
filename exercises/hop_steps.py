"""
Taken from "Cracking the Coding Interview" book by GayleMcDowell, 2015.

A child is running up a staircase with n steps and can hop either 1 step, 2 steps,
 or 3 steps at a time. Implement a method to count how many possible ways the child
 can run up the stairs.
"""

from techniques.memoization import memoize


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


print(count_ways(1))
print(count_ways(2))
print(count_ways(3))
print(count_ways(5))
print(count_ways(7))
print(count_ways(25))
