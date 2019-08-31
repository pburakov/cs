"""
Candies
=======

There are :math:`n` children standing in a line. Each child is assigned a rating value
according to their average grade as a set :math:`R`. As their teacher, you want to reward
the children with candies. However children are known to get jealous, and you want to be
fair.

Candies distribution is subjected to the following requirements:

    - each child must have at least one candy.
    - children with a higher rating get more candies than their neighbors.

What is the minimum number of candies you must give while keeping children happy?

Example::

    [1, 2, 2] -> 4  # Optimal distribution is [1, 2, 1]
    [2, 4, 2, 6, 1, 7, 8, 9, 2, 1] -> 19  # [1, 2, 1, 2, 1, 2, 3, 4, 2, 1]

"""


def candies(R):
    """Returns minimum amount of candies based on input ratings.

    The algorithm starts with everyone having one candy. Then it makes two passes: from
    left to right and from right to left and compares each value with the previous one
    (adjacent child). All possible rating discrepancies will be caught by one of the two
    loops. The computed sum of candies is returned.

    Complexity:
        :math:`O(n)` running time, :math:`O(n)` for storage.

    :param list R: List of ratings.
    :return: Minimum amount of candies.

    """
    n = len(R)
    C = [1] * n  # Allocating array for candies distribution
    for i in range(1, n):
        if R[i] > R[i - 1]:
            C[i] = C[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if R[i] > R[i + 1]:
            # By using max() we're making sure we're not breaking
            # the values set by the first loop.
            C[i] = max(C[i], C[i + 1] + 1)
    return sum(C)
