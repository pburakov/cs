"""
Sudoku is a popular combinatorial problem.

A standard Sudoku puzzle contains 81 cells, in a 9 by 9 grid, and has 9 zones, each zone being the intersection of the first, middle, or last 3 rows, and the first, middle, or last 3 columns. Each cell may contain a number from one to nine; each number can only occur once in each zone, row, and column of the grid. Pre-filled cells are provided as clues.

Backtracking algorithm follows a familiar pattern:
 1) Construct a partial solution for first unfilled cell.
 2) Try this solution.
 3) If it worked for the board so far - continue, otherwise - backtrack.
Repeat 1 to 3 until all cells are filled out.
"""


def solve(B):
    """
    Sudoku puzzle solver.

    Sudoku puzzle board is represented by two-dimensonal array of integers of size `9`x`9`.

    :param list[list[int]] B: Sudoku board
    :return None: Prints to stdout
    """
    if has_solution(B):
        print_board(B)
    else:
        print("Board has no solution")


"""
Auxiliary routines and constants used in the solution
"""
BOARD_EDGE_SIZE = 9
ZONE_SIZE = 3


def has_solution(B, x=0, y=0):
    """
    Evaluates if Sudoku board can be solved.

    This is a exhaustive Sudoku board solution search. Every digit is tried for every unfilled cell. Those that don't lead to a legit solution are dropped and board state backtracked.

    Complexity: O(10^(b*b-k)) where `n` is a board edge and `k` is number of clues (filled cells). Algorithm works through increasingly more cycles when searching for Sudokus with 20 clues or fewer. Puzzles with 17 clues are notoriously difficult to find. When the constraint of symmetry is applied, the expected search time will dramatically increase yet further.
    :param list[list[int]] B: Current state of Sudoku board
    :param int x: Row to start solution construction (used in recursion)
    :param int y: Column to start solution construction (used in recursion)
    :return bool: Returns True if board has a solution, False otherwise
    """
    if x == BOARD_EDGE_SIZE:  # Go to next row
        x = 0
        y += 1
    if y == BOARD_EDGE_SIZE:
        return True  # Reached the end, solution has been found
    else:
        if B[x][y] == 0:
            # Construct candidates
            for i in range(1, 10):
                if valid_zone(B, i, x, y) and valid_row(B, i, x) and valid_col(B, i, y):
                    B[x][y] = i
                    if has_solution(B, x + 1, y):
                        return True
                    else:  # Backtrack if a candidate doesn't lead to a solution
                        B[x][y] = 0
            return False
        else:
            return has_solution(B, x + 1, y)


def valid_zone(B, e, x, y):
    """
    Check candidate validity in a Sudoku board zone..

    Will return True if value is not present in the candidate zone, False otherwise.

    Complexity: O(1), bound by a constant zone size
    :param list[list[int]] B: Sudoku board
    :param int e: Candidate value to validate
    :param int x: Row coordinate of a value
    :param int y: Column coordinate of a value
    :return bool: Validation result
    """
    for i in range(x - x % ZONE_SIZE, x - x % ZONE_SIZE + ZONE_SIZE):
        for j in range(y - y % ZONE_SIZE, y - y % ZONE_SIZE + ZONE_SIZE):
            if B[i][j] == e:
                return False
    return True


def valid_row(B, e, r):
    """
    Check candidate validity in a Sudoku board row.

    Will return True if value is not present in the candidate row, False otherwise.

    Complexity: O(1), bound by a constant board edge size
    :param list[list[int]] B: Sudoku board
    :param int e: Candidate value to validate
    :param int r: Row coordinate of a value
    :return:
    """
    for i in range(0, BOARD_EDGE_SIZE):
        if B[r][i] == e:
            return False
    return True


def valid_col(B, e, c):
    """
    Check candidate validity in a Sudoku board column.

    Will return True if value is not present in the candidate column, False otherwise.

    Complexity: O(1), bound by a constant board edge size
    :param list[list[int]] B: Sudoku board
    :param int e: Candidate value to validate
    :param int c: Column coordinate of a value
    :return:
    """
    for i in range(0, BOARD_EDGE_SIZE):
        if B[i][c] == e:
            return False
    return True


def print_board(B):
    """
    Prints out board.

    :param list[list[int]] B: Sudoku board
    :return None: Prints to stdout
    """
    for row in B:
        for x in row:
            print(x, end=' ')
        print()
