"""
Knight's Tour
=============

Knight's tour is a common mathematical puzzle given to CS students.

Given a chessboard of size :math:`n \\times n` and the starting coordinates, find a
sequence of moves of a knight, such that the knight visits every square only once.

The solution to a Knight Tour problem is an interesting intersection of a combinatorial
search problem and a graph search algorithm.
"""


def knight_tour(n, y, x):
    """Recursive solution of Knight's tour problem with Warnsdorff heuristic.

    The chess board is represented by a two-dimensional matrix of size :math:`n \\times n`.
    The path is represented by a consecutive move numbers on the board, starting with `1`.
    The board is printed out once a solution is found.

    Complexity:
        :math:`O(n)`, due to the use to Warnsdorff heuristic.

    :param int n: Board size.
    :param int y: Starting square vertical coordinate.
    :param int x: Starting square horizontal coordinate.

    """
    B = init_board(n)
    B[x][y] = 1  # First move
    if has_solution(B, x, y, 2):
        print_board(B)
    else:
        print("No solution")


def has_solution(B, y, x, m):
    """Backtracking sub-routine for solving knight's tour problem.

    Exhaustively searches for first solvable paths starting at square :math:`(x,y)` using
    DFS-like backtracking algorithm with the use of Warnsdorff heuristic

    Note that the use of recursion is suboptimal and may cause stack exhaustion for a large
    :math:`n`. Backtracking is used for the purpose of code clarity, but can be refactored
    to iteration, using saved state of the board :math:`B`.

    Complexity:
        :math:`O(n^2)` for a backtracking algorithm, where :math:`n` is the size of
        the board. The use of Warnsdorff heuristic, however, allows to locate the
        first solution in :math:`O(n)` time.

    :param list[list[int]] B: Chess board.
    :param int y: Starting square vertical coordinate.
    :param int x: Starting square horizontal coordinate.
    :param int m: Current move number.
    :return: :data:`True` if board is solvable with such position of the knight.

    """
    n = len(B)
    if m == n * n + 1:  # Final move, a solution is found
        return True
    else:
        moves = legal_moves(B, y, x)
        for yy, xx in sort_onward(B, moves):  # Moves are sorted with Warnsdorff's rule
            B[yy][xx] = m  # Saving the move
            if has_solution(B, yy, xx, m + 1):
                return True  # Next move has a solution
            else:
                B[yy][xx] = 0  # Backtracking in case of an illegal move
        return False  # Could not find a move leading to a solution from given coordinates


def legal_moves(B, y, x):
    """Lists square coordinates for legal moves from the given starting square.

    Complexity:
        :math:`O(1)`. Will yield at most :math:`8` coordinates.

    :param list[list[int]] B: Chess board.
    :param int y: Starting square vertical coordinate.
    :param int x: Starting square horizontal coordinate.
    :return: List of square coordinates for onward move options.

    """
    offsets = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    n = len(B)
    out = []
    for y1, x1 in offsets:
        yy = y + y1
        xx = x + x1
        if 0 <= yy < n and 0 <= xx < n:
            if B[yy][xx] == 0:
                out.append((yy, xx))
    return out


def sort_onward(B, M):
    """Sorts list of moves in accordance with Warnsdorff's heuristic.

    Warnsdorff's rule is a heuristic for finding a knight's tour, which greatly reduces
    the cost of finding the first legal solution. The knight always proceeds to the square
    from which it will have the fewest onward moves.

    Complexity:
        :math:`O(1)`, is bound by a constant, since there are at most :math:`8` legal
        moves for each coordinate.

    :param list B: Chess board.
    :param list M: List of moves.
    :return: List of onward moves, sorted in accordance with Warnsdorf's heuristic,
     starting with a square with the fewest onward moves.

    """
    return sorted(M, key=lambda t: len(legal_moves(B, t[0], t[1])))


def init_board(n):
    """Builds an empty rectangular two-dimensional matrix filled with zeroes.

    Complexity:
        :math:`O(n^2)`.

    :param int n: Edge size.
    :return: An empty two-dimensional matrix filled with zeroes.

    """
    return [[0 for _ in range(n)] for _ in range(n)]


def print_board(B):
    """Prints out the two-dimensional matrix.

    Example::

        23   10   15    4   25
        16    5   24    9   14
        11   22    1   18    3
         6   17   20   13    8
        21   12    7    2   19

    Complexity:
        :math:`O(n^2)`.

    :param list[list] B: Input matrix.

    """
    for line in B:
        for square in line:
            print("{:5d}".format(square), end='')
        print()
