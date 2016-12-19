"""
Knight's Tour
=============

Knight tour is a famous mathematical puzzle often given to CS students.

Given a chessboard of size :math:`n × n` and a starting coordinates, find a sequence of
moves of a knight, such that the knight visits every square only once.

Proposed solution to a Knight Tour problem is an interesting intersection of a
combinatorial search problem and a graph path search algorithm.
"""


def solution(n, x, y):
    """Recursive solution of Knight's tour problem with Warnsdorff heuristic.

    The chess board is represented by a two-dimensional array of size :math:`n × n`. Path
    is represented by a consecutive move numbers on the board, starting with `1`. The
    board is printed out once a solution is found.

    Complexity:
        :math:`O(n)`, thanks to Warnsdorff heuristic, see implementation comments.

    :param int n: Board size.
    :param int x: Starting coordinate :math:`x`.
    :param int y: Starting coordinate :math:`y`.

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
    """Backtracking sub-routine for knight tour solution.

    Exhaustively searches for first solvable paths using DFS-like backtracking algorithm
    with the implementation of Warnsdorff heuristic.

    Note that the use of recursion is suboptimal and may cause stack exhaustion for large
    :math:`n`. Backtracking is used for the purpose of code clarity, but can be easily
    refactored to iteration, using saved copies of the state of the board :math:`B`.

    Complexity:
        :math:`O(k^{n^2})` for a normal backtracking algorithm, where :math:`n` is the
        size of the board and :math:`k` is operations for calculating and sorting legal
        moves, bound by a constant. Warnsdorff heuristic allows to locate the first
        solution in :math:`O(n)` time.

    :param list[list[int]] B: Mutable board representation.
    :param int x: Starting coordinate :math:`x`.
    :param int y: Starting coordinate :math:`y`.
    :param int m: Current move number.
    :return: :data:`True` if board is solvable with such position of the knight.

    """
    n = len(B)
    if m == n * n + 1:  # Final move, solution is found
        return True
    else:
        moves = legal_moves(B, x, y)
        for xx, yy in sort_onward(B, moves):  # Moves are sorted using Warnsdorff's rule
            B[xx][yy] = m  # Saving the move
            if has_solution(B, xx, yy, m + 1):
                return True  # Next move has a solution
            else:
                B[xx][yy] = 0  # Backtracking in case of illegal move
        return False  # Could not find a move leading to a solution from given coordinates


def legal_moves(B, x, y):
    """Lists legal coordinates for a move from given starting coordinates and the board.

    Complexity:
        :math:`O(1)`. Will yield at most :math:`8` such coordinates.

    :param list[list[int]] B: List board representation.
    :param int x: Starting coordinate :math:`x`.
    :param int y: Starting coordinate :math:`y`.
    :return: List of coordinates for legit next move options.

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
    """Sorts list of moves in accordance with Warnsdorff's heuristic.

    Warnsdorff's rule is a heuristic for finding a knight's tour, which greatly reduces
    the cost of finding the first legal solution. The knight is moved so that it always
    proceeds to the square from which the knight will have the fewest onward moves. This
    algorithm sorts onward moves 2 levels deep.

    Great visualization for Warnsdorff heuristic can be found `here`_

    .. _here: http://warnsdorff.com

    Complexity:
        :math:`O(1)`, is bound by a constant, since there are at most :math:`8` legal
        moves for each coordinate.

    :param list[list[int]] B: List board representation.
    :param list[(int, int)] M: List of moves.
    :return: List of onward moves, sorted in accordance with Warnsdorf's heuristic from
     fewer legal moves to most legal moves.

    """
    return sorted(M, key=lambda t: len(legal_moves(B, t[0], t[1])))


def init_board(n):
    """Builds an empty chess board representation.

    Every cell will contain 0, meaning no moves were made from every cell.

    Complexity:
        :math:`O(n^2)`.

    :param int n: Board size.
    :return: 2-D :data:`list` board representation.

    """
    return [[0 for _ in range(n)] for _ in range(n)]


def print_board(B):
    """Prints out board with moves map.

    Example::

        23   10   15    4   25
        16    5   24    9   14
        11   22    1   18    3
         6   17   20   13    8
        21   12    7    2   19

    Complexity:
        :math:`O(n^2)`.

    :param list[list[int]] B: List board representation.

    """
    for line in B:
        for row in line:
            print("{:5d}".format(row), end='')
        print()
