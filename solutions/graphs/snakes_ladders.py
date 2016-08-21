def solution(M):
    from basic_data_structures.queue import Queue, enqueue, dequeue, next as peek
    visited = [False] * (len(M) + 1)
    visited[0] = True
    q = Queue(len(M))
    move = Move(0, 0)
    enqueue(q, move)
    while q.length > 0:
        move = peek(q)
        i = move.cell  # cell no.
        d = move.dist
        if i == len(M) - 1:
            break
        dequeue(q)
        for dice in range(1, 4):
            next_i = i + dice
            if next_i < len(M):
                if visited[next_i] is False:
                    visited[next_i] = True
                    if M[next_i] == 0:
                        enqueue(q, Move(next_i, d + 1))
                    else:
                        enqueue(q, Move(M[next_i], d + 1))
    return move.dist


class Move:
    def __init__(self, c, d):
        self.cell = c
        self.dist = d


m1 = [0, 3, 0, 0, 2, 3, 0, 0]
print(solution(m1))
