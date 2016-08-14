"""
This is a word production sequence problem, better known as word ladder. It can be found
 in many different flavours. Although it involves strings, it is a great example how
 simple graph algorithms can be used to solve various seemingly unrelated problems.

You are given a dictionary of words of the same lengths, consisting of lowercase letters.
 Example: `{"hot","hit","dot","dog","cog","lot","log"}`. Given a starting word and a
 target word, find the shortest available transformation sequence, if such exists. Two
 rules have to be maintained:
  - at each step only a single letter can be changed at a time,
  - every word in a sequence must exist in a dictionary.

Example ladder: `"hit" -> "hot" -> "dot" -> "dog" -> "cog"` of length of 5.
"""


def solution(D, s, t):
    """
    Word ladder solver using BFS shortest path.

    This solution takes advantage of a property of BFS algorithm. If we follow parent
     pointers (a vertex from which other vertex was visited) in a breadth-first tree, we
     can reconstruct the shortest path between two vertices. Let every word in a
     dictionary be a vertex in a graph. If we determine the path from `s` to `t` and
     reconstruct it, we'll get the exact word production sequence.

    Note, that this solution can be altered to return an integer distance without the
     path reconstruction.

    Complexity: O(Dm), see the copmlexity of the BFS subroutine.
    :param set D: Dictionary (set) of words
    :param str s: Starting string
    :param str t: Target string
    :return list: Production sequence
    """
    stack, out = [], []  # Sequence stack and the output list
    v = build(D, s, t)  # Return `v.distance` for path length
    # Getting production sequence backwards by reconstructing BFS path
    while v is not None:
        stack.append(v.candidate_string)
        v = v.parent
    # Building output by reversing a stack
    while len(stack) > 0:
        out.append(stack.pop())
    return out


def build(D, s, t):
    """
    Words production sequence path builder using BFS algorithm.

    This BFS sub-routine connects vertices in a graph, writes parent pointers and
     distance from the source string.

    Complexity: O(D+Dm) from BFS, where `D` is the number of words in the dictionary and
     `m` is the length of words used. Time devoted to construction of candidate strings
     is constant bound to the alphabet size. The number of edges in the worst case is
     `D^2`.
    :param set D: Dictionary (set) of words
    :param str s: Source string
    :param str t: Target string
    :return Vertex|None: Vertex containing target string (if found)
    """
    from queue import Queue
    Q = Queue()
    D.remove(s)  # Remove used word from a dictionary
    Q.put(Vertex(s, 0))
    while Q.empty() is False:
        v = Q.queue[0]  # Peek at queue
        if v.candidate_string == t:
            return v  # Target is found
        cs = list(v.candidate_string)  # Converting to list, strings are immutable
        # Try all possible permutations of a candidate string
        for i in range(0, len(cs)):
            for c in ALPHABET:
                cs[i] = c
                cs_as_str = "".join(cs)
                if cs_as_str in D:
                    D.remove(cs_as_str)
                    Q.put(Vertex(cs_as_str, v.distance + 1, v))
            cs[i] = v.candidate_string[i]
        Q.get()  # Pop from queue
    return None


"""
Constants and data structures used in the solution
"""


class Vertex:
    def __init__(self, s, d, p=None):
        """
        Graph vertex representing candidate string with a distance value.

        :param str s: Candidate string
        :param int d: Distance
        :param Vertex p: Parent vertex
        """
        self.candidate_string = s
        self.distance = d
        self.parent = p


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
