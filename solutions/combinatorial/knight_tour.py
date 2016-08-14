"""
Knight tour is famous mathematical puzzle often given to CS students.

Given a chessboard of size `n` x `n` and a starting coordinates, find a sequence of moves of a knight, such that the knight visits every square only once.
"""


def solution(n, x, y):
    """


    :param int n: Board size
    :param int x: Starting coordinate `x`
    :param int y: Starting coordinate `y`
    :return None: Prints to stdout
    """
    B = init_board(n)
    B[x][y] = 1  # First move
    if has_solution(B, x, y, 2):
        print_board(B)
    else:
        print("No solution")


"""
Auxiliary routines used in the solution
"""


def has_solution(B, x, y, m):
    """
    Backtracking sub-routine for knight tour solution.



    :param list[list[int]] B: List board representation
    :param int x: Starting coordinate `x`
    :param int y: Starting coordinate `y`
    :param int m: Current move
    :return bool: Returns true if board is solvable with such position of the knight
    """
    n = len(B)
    if m == n * n + 1:  # Final move
        return True
    else:
        moves = legal_moves(B, x, y)
        for xx, yy in sort_onward(B, moves):
            B[xx][yy] = m
            if has_solution(B, xx, yy, m + 1):
                return True
            else:  # Backtracking in case of illegal move
                B[xx][yy] = 0
        return False  # Could not move from such `x, y` coordinates


def legal_moves(B, x, y):
    """
    Lists legal coordinates for a move from given starting coordinates and the board.

    Complexity: O(1). Will yield at most 8 such coordinates.
    :param list[list[int]] B: List board representation
    :param int x: Starting coordinate `x`
    :param int y: Starting coordinate `y`
    :return list[(int, int)]: Coordinates of onward legit moves
    """
    offsets = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    n = len(B)
    out = []
    for x1, y1 in offsets:
        xx = x + x1
        yy = y + y1
        if 0 <= xx < n and 0 <= yy < n:
            if B[xx][yy] == 0:
                out.append((xx, yy))
    return out


def sort_onward(B, M):
    """
    Sorts list of moves in accordance with Warnsdorf's heuristic rule.

    Warnsdorf's rule is a heuristic for finding a knight's tour that greatly increases the speed of finding a legal solution. The knight is moved so that it always proceeds to the square from which the knight will have the fewest legit onward moves.

    Complexity: O(m log(m)) where `m` is the number of moves.
    :param list[list[int]] B: List board representation
    :param list[(int, int)] M: List of moves
    :return list[(int, int)]: List `M` sorted in accordance with Warnsdorf's heuristic from fewer moves to most moves
    """
    return sorted(M, key=lambda t: len(legal_moves(B, t[0], t[1])))


def init_board(n):
    """
    Builds an empty chess board representation cells containing 0.

    :param int n: Board size
    :return list[list[int]]: List board representation
    """
    return [[0 for _ in range(n)] for _ in range(n)]


def print_board(B):
    """
    Prints out list board representation.

    :param list[list[int]] B: List board representation
    :return None: Prints to stdout
    """
    for line in B:
        for row in line:
            print("{:3d}".format(row), end='')
        print()
