"""
Yoda Reverse
============

Write an algorithm to reverse the words in a string, keeping punctuation symbols in the
original order.

Example::

    Input: "You must learn, padawan. The force is strong!"
    Output: "strong is force, The. padawan learn must You!"

"""


def solve(S):
    """Yoda Reverse problem solver.

    The algorithm first tokenizes the string. It puts every word and punctuation mark into
    an array in their original order. The array is then traversed with two pointers, one
    starting at the beginning, another one at the end. Words at the pointers are swapped,
    but punctuation symbols are skipped. The output string is constructed.

    Complexity:
        :math:`O(n)` where :math:`n` is a number of characters in a string.

    :param str S: Input string.
    :return: Reversed string.

    """
    tokens = []  # Array of words and punctuation symbols
    word = ''
    for i in range(len(S)):
        c = S[i]
        if valid_letter(c):
            word += c
        else:
            if len(word) > 0:
                tokens.append(word)
            if c != ' ':
                tokens.append(c)
            word = ''
    i = 0
    j = len(tokens) - 1
    out = ''
    while i < len(tokens) and j >= 0:
        if valid_word(tokens[j]):
            if out != '':
                out += ' '
            out += tokens[j]
        if not valid_word(tokens[i]):
            out += tokens[i]
        i += 1
        j -= 1
    return out


"""
Auxiliary routines used in the solution.
"""


def valid_letter(c):
    """Evaluates if input character is a letter.

    Complexity:
        :math:`O(1)` for constant character code comparison.

    :param str c: Input character.
    :return: :data:`True` if character is a letter, :data:`False` otherwise.

    """
    return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z')


def valid_word(word):
    """Evaluates if string contains only letters.

    Complexity:
        :math:`O(c)` where :math:`c` is number of characters in the string.

    :param str word: Input string.
    :return: :data:`True` if string is valid, :data:`False` otherwise.

    """
    for c in word:
        if not valid_letter(c):
            return False
    return True
