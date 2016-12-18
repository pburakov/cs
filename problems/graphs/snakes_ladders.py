"""
# Snakes and Ladders

Implement an algorithm that will find the minimum amount of dice throws required to win
 "Snake and Ladders" game.

Game board is represented by an array with non-zero values representing index where the
 player will have to jump if he/she lands on that cell.

Example:
```
M = [0, 0, 0, 7, 2, 0, 0, 0, 5, 0]
Output: 2
```
"""


def solution(M):
    """
    Snake and Ladders minimum moves solver.

    Every throw of dice generates one move possibility. Together they form a graph of all
     possible moves and associated distance, or number of preceding moves required to
     reach that cell. Using simple breadth-first search algorithm we'll be able to find
     the shortest distance to the last cell.

    Complexity: O(V+E) where `V` is number of cells and `E` is number of possible "jumps"
    :param list[int] M: List board representation
    :return int: Minimum amount of dice throws required to reach the final cell
    """
    from basic.fifo import Queue, enqueue, dequeue, next as peek

    visited = [False] * (len(M) + 1)  # Map of visited cells
    visited[0] = True
    q = Queue(len(M))
    move = Move(0, 0)  # Generate first move
    enqueue(q, move)
    while q.length > 0:
        move = peek(q)
        if move.cell == len(M) - 1:
            break  # Reached the end, `move` is the last cell
        dequeue(q)
        for dice in range(1, 7):  # Try all the dice throws
            next_i = move.cell + dice
            if next_i < len(M):
                if visited[next_i] is False:
                    visited[next_i] = True
                    if M[next_i] == 0:
                        enqueue(q, Move(next_i, move.dist + 1))
                    else:
                        enqueue(q, Move(M[next_i], move.dist + 1))
    return move.dist


"""
Data structures used in the solution
"""


class Move:
    def __init__(self, c, d):
        """
        Snakes and Ladders move representation.

        :param int c: Cell number (index)
        :param int d: Distance (number of moves)
        """
        self.cell = c
        self.dist = d
