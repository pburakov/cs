"""
Snakes and Ladders
==================

Implement an algorithm that will find the minimum amount of dice throws required to win
a "Snake and Ladders" game.

Game board is represented by an array with non-zero values representing the index to which
the player will have to jump to if he/she lands on that cell. Normal cells are marked with
:math:`0`.

Example::

    [0, 0, 0, 7, 2, 0, 0, 0, 5, 0] -> 2

"""


def minimum_throws(M):
    """Calculates the minimum amount of dice throws required to win a game board.

    Every throw of a dice generates a m possibility. Together they form a graph of all
    possible moves with an associated distance. The distance is the number of preceding
    moves required to reach that cell. Using BFS-like algorithm we'll be able to find the
    shortest distance to the last cell.

    Complexity:
        :math:`O(V+E)` where :math:`V` is number of cells and :math:`E` is number of
        possible "jumps".

    :param list M: Game board.
    :return: The minimunm amount of dice throws required to win the game board.

    """
    from basic.fifo import Queue
    from basic.fifo import enqueue, dequeue, next as peek

    visited = [False] * (len(M) + 1)  # Map of visited cells
    visited[0] = True
    Q = Queue(len(M))
    m = Move(0, 0)  # Generate first move
    enqueue(Q, m)
    while Q.length > 0:
        m = peek(Q)
        if m.i == len(M) - 1:
            break  # Reached the last cell
        dequeue(Q)
        for t in range(1, 7):  # Try all the dice throws
            next_i = m.i + t
            if next_i < len(M):
                if visited[next_i] is False:
                    visited[next_i] = True
                    if M[next_i] == 0:
                        enqueue(Q, Move(next_i, m.d + 1))
                    else:
                        enqueue(Q, Move(M[next_i], m.d + 1))
    return m.d


class Move:
    """A move vertex in a game search space.
    """

    def __init__(self, i, d):
        """A move vertex in a game search space.

        :param int i: Cell index.
        :param int d: Distance, number of moves it took to reach the cell.

        """
        self.i = i
        self.d = d
