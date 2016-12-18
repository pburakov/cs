"""
# N Queens

N-queens is the problem of placing `n` chess queens on an `n`×`n` chessboard so that no
 two queens threaten each other. Thus, a solution requires that no two queens share the
 same row, column, or diagonal.

There are no solutions for `n` less than 4. Interestingly, the 6-queens puzzle has fewer
 solutions than the 5-queens puzzle. There are 22,317,699,616,364,044 solutions for
 `n=26`.
"""


def solution(n):
    """
    Solves N-queens problem for n-sized board.

    There are various ways to solve this problem. This solution uses combinatorial search
     of all possible permutations of a one-dimensional array of unique integers, with an
     addition of pruning a recursive branch when has an invalid state.

    Since queens cannot share same row or column, one of the dimensions can be taken out
     of the problem completely. Each generated permutation is checked for validity of a
     solution. Complete 2-dimensional board can be easily reconstructed once the
     solution is found.

    Complexity: There is currently no known formula for the exact number of solutions,
     or even for its asymptotic behaviour.
    :param int n: Number of queens and dimension of the board
    :return None: Solution is printed to Std out
    """
    if n < 4:
        raise ValueError("No solution for n < 4")
    else:
        B = [k for k in range(0, n)]  # Constructs set {0,1,2,...,n}
        P = []  # Output list of all solutions
        permute_board(B, P)
        for b in P:
            printout(b)


"""
Auxiliary routines used in the solution
"""


def permute_board(B, P, i=0):
    """
    Exhaustively searches for all "valid" solutions of a board.

    Permutes all possible combinations of queen placements. Search assumes that elements
     beyond `i` form a correct solution.

    Complexity: Asymptotic boundary is unknown.
    :param list[int] B: Input list with no repeating elements
    :param list[list] P: Output list of valid queen placements in 1-dimensional board
     list representations
    :param int i: Current index (used in recursion)
    :return None: List `P` is updated
    """
    n = len(B)
    if i == n:
        P.append(B.copy())
    else:
        for k in range(i, n):
            B[i], B[k] = B[k], B[i]
            # Do not recurse if board is already invalid
            if valid_board(B, i):
                permute_board(B, P, i + 1)
            B[i], B[k] = B[k], B[i]


def valid_board(B, i):
    """
    Evaluates validity of queens placement on a board.

    Checks if no queens are in line of attack of each other. Returns True if board
     beyond `i` has already been built valid.

    Complexity: O(1) to O(i). Insignificant routine compared to the rest of the
     solution.
    :param list[int] B: Queen placements in 1-dimensional board list representation
    :param int i: Current index
    :return bool: Evaluation result
    """
    for k in range(0, i):
        if abs(B[i] - B[k]) == i - k:
            return False
    return True


def printout(B):
    """
    Prints out board.

    Complexity: O(n^2) for one solution, where `n` is the size of the board
    :param list[int] B: Queen placements in 1-dimensional board list representation
    :return None: Output is printed to Std out
    """
    n = len(B)
    # Top border
    for i in range(0, n):
        print("+-", end='')
    print('+')
    # Rows
    for y in range(n - 1, -1, -1):
        print("|", end='')
        # Queens placement
        for x in B:
            if x == y:
                print("Q|", end='')
            else:
                print(" |", end='')
        print()
    # Bottom border
    for i in range(0, n):
        print("+-", end='')
    print('+')
