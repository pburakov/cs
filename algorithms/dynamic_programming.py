"""
Here are several problems and their solutions that illustrate and use the
 dynamic programming approach.

A DP is an algorithmic technique which is usually
 based on a recurrent formula and one (or some) starting states. A sub-solution
 of the problem is constructed from previously found ones. DP solutions have a
 polynomial complexity which assures a much faster running time than other
 techniques like backtracking, brute-force etc.
"""

"""
Given a list of N coins, their values (V1, V2, … , VN), and the total sum S.
Find the minimum number of coins the sum of which is S (we can use as many
coins of one type as we want), or report that it’s not possible to select
coins in such a way that they sum up to S.
"""


def min_coins(coins, S):
    solutions = [S] * (S + 1)
    solutions[0] = 0
    for s in range(1, S + 1):
        for V in coins:
            if 0 <= s - V < len(solutions):
                if V == s or solutions[s - V] + 1 < solutions[s]:
                    solutions[s] = solutions[s - V] + 1
    return solutions[S]


print(min_coins([1, 3, 5], 1))
print(min_coins([1, 3, 5], 5))
print(min_coins([1, 3, 5], 7))
print(min_coins([1, 3, 5], 10))
print(min_coins([1, 3, 5], 123))
