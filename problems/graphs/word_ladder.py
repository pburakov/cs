"""
Word Ladder
===========

You are given a dictionary of words of same lengths :math:`D`, consisting of lowercase
letters. Given a starting word :math:`s` and a target word :math:`t`, find the shortest
available transformation sequence, if such exists.

Two rules have to be maintained:

    - at each step only a single letter can be changed at a time;
    - every word in a sequence must exist in a dictionary.

Example::

    (D={"hot","hit","dot","dog","cog","lot","log"},
     s="hit",
     t="cog") -> ["hit","hot", "dot", "dog", "cog"]

This is a word production sequence problem, better known as the word ladder. It can be found
in many different disguises. It is a great example of how simple graph algorithms can be
used to solve various seemingly unrelated problems.

"""
from basic.fifo import Queue
from basic.fifo import enqueue, dequeue, next as peek


def word_ladder(D, s, t):
    """Computes the word production sequence.

    The solution takes an advantage of an important property of a BFS algorithm. If we
    follow parent pointers (a vertex from which the other vertex was visited) from a target
    vertex to a source vertex in a breadth-first tree, we can reconstruct the shortest path
    between the two vertices. Let every word in a dictionary be a vertex in a graph. If we
    determine the path from :math:`s` to :math:`t` and reconstruct it, we'll get the exact
    word production sequence.

    Complexity:
        :math:`O(|D|m)`, where :math:`m` is the maximum length of words in a dictionary.

    :param set D: Dictionary of words.
    :param str s: Starting word.
    :param str t: Target word.
    :return: World production sequence.

    """
    stack, out = [], []  # Sequence stack and the output list
    v = build_sequence(D, s, t)  # Return `v.distance` for path length
    # Getting production sequence backwards by reconstructing BFS path
    while v is not None:
        stack.append(v.s)
        v = v.p
    # Building output by reversing a stack
    while len(stack) > 0:
        out.append(stack.pop())
    return out


def build_sequence(D, s, t):
    """Builds word production sequence.

    This BFS routine connects vertices in a search graph and computes distance from the
    source string to a target string.

    Complexity:
        :math:`O(|D|m)`, where :math:`m` is the maximum length of words in a dictionary.
        Time devoted to the construction of candidate words is constant, bound to the
        available alphabet.

    :param set D: Dictionary of words.
    :param str s: Source word.
    :param str t: Target word.
    :return: A target word vertex, if found.

    """
    n = len(D)
    A = build_alphabet(D)  # Optimized alphabet uses only letters from the dictionary
    Q = Queue(n)
    D.remove(s)  # Remove used word from a dictionary
    enqueue(Q, Candidate(s, 0))
    while Q.length > 0:
        v = peek(Q)
        if v.s == t:
            return v  # Target is found
        w = list(v.s)  # Candidate word as a list of characters
        # Try all possible permutations of characters in a candidate word
        for i in range(0, len(w)):
            for c in A:
                w[i] = c
                ws = "".join(w)  # Candidate word as a string
                if ws in D:
                    D.remove(ws)  # Remove used word from a dictionary
                    enqueue(Q, Candidate(ws, v.d + 1, v))
            w[i] = v.s[i]  # Revert explored character
        dequeue(Q)
    return None


def build_alphabet(D):
    """Returns a set of letters used in a dictionary.

    :param set D: Dictionary of words.
    :return: Set of letters used in the dictionary.

    """
    A = set()
    for word in D:
        for c in word:
            A.add(c)
    return A


class Candidate:
    """A candidate word vertex in a word ladder search space.
    """

    def __init__(self, s, d, p=None):
        """A candidate word vertex in a word ladder search space.

        :param str s: Candidate word.
        :param int d: Distance from a source word.
        :param Candidate p: Parent vertex.
        """
        self.s = s
        self.d = d
        self.p = p

    def __str__(self):
        return self.s
