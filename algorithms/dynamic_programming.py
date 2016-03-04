"""
Here are several problems and their solutions that illustrate and use the
 dynamic programming approach. Taken from TopCoder DP Tutorial.

A DP is an algorithmic technique which is usually
 based on a recurrent formula and one (or some) starting states. A sub-solution
 of the problem is constructed from previously found ones. DP solutions have a
 polynomial complexity which assures a much faster running time than other
 techniques like backtracking, brute-force etc.
"""

"""
1. Given a list of N coins, their values (V1, V2, … , VN), and the total sum S.
 Find the minimum number of coins the sum of which is S (we can use as many
 coins of one type as we want), or report that it’s not possible to select
 coins in such a way that they sum up to S.
"""


def min_coins(coins, S):
    solutions = [len(coins) + 1] * (S + 1)
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

"""
2. A table `A` composed of `n` x `m` cells, each having a certain quantity of
 apples, is given. You start from the upper-left corner. At each step you can go
 down or right one cell. Find the maximum number of apples you can collect.
"""


def max_apples(A):
    n = len(A)
    m = len(A[0])
    S = [[0 for j in range(m)] for h in range(n)]
    for i in range(0, n):
        for k in range(0, m):
            S[i][k] = A[i][k]
            try:
                # Out of bounds error
                S[i][k] += max(S[i][k - 1], S[i - 1][k], 0)
            except Exception as e:
                pass
    return S[n - 1][m - 1]


print(max_apples([
    [2, 1],
    [1, 2]
]))
print(max_apples([
    [1, 2, 1, 8],
    [5, 3, 5, 6],
    [3, 7, 1, 2]
]))
