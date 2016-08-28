"""
I've been asked this problem when I was interviewing at Google. Given a simple syntax using numbers and square brackets, parse a given expression into a complete string.

Input: `ab4c`. Output: `abcccc`
Input: `1a1b0c`. Output: `ab`
Input: `2[abc]`. Output: `abcabc`
Input: `2[ab3[cd]]x3yz`. Output: `abcdcdcdabcdcdcdxyyyz`
"""


def solution(S):
    """

    :param str S:
    :return str:
    """
    parse_tree = tokenize(S)
    return reconstruct(parse_tree)


"""
Auxiliary routines used in the solution
"""


def tokenize(S):
    """

    Tokenization algorithm is based on a finite string automata. It has 3 states:
     a) Parse digits into integer values (collected number is kept as number of pattern of repetitions for the next state)
     b) Tokenize parenthesized expression (expression is recursively tokenized)
     c) Tokenize single character

    State of the automata is triggered based on a character encountered. State is held until another trigger is occurred.

    Complexity: O(n*b) where `b` is number of opening brackets that spawns nested string traversal
    :param str S:
    :return str:
    """
    n = len(S)
    buffer = []
    repetitions = 1  # Repeat each token once by default
    i = 0  # Traversal index
    while i < n:
        if S[i] in NUMBERS:
            # Switch automata to numbers matching mode
            repetitions = 0
            while i < n and S[i] in NUMBERS:
                # Fast-forward to the nearest non-numeric character
                repetitions = repetitions * 10 + int(S[i])
                i += 1
        elif S[i] == OPENING_BRACKET:
            # Switch automata to expression tokenization mode
            open_brackets = 1
            i += 1  # Move past current opening bracket
            start = i
            end = i + 1
            while i < n and open_brackets > 0:
                # Fast-forward to a matching closing bracket
                if S[i] == OPENING_BRACKET:
                    open_brackets += 1
                if S[i] == CLOSING_BRACKET:
                    open_brackets -= 1
                end = i
                i += 1
            buffer.append(tokenize(S[start:end]) * repetitions)
            repetitions = 1
        else:
            buffer.append(S[i] * repetitions)
            repetitions = 1
            i += 1
    return buffer


def reconstruct(T):
    """
    Builds final string off a list of tokens.

    Complexity: O(n) where `n` is length of a final string
    :param list T: Tokenized expression
    :return str: Final string
    """
    out = ''
    for t in T:
        if type(t) is list:
            t = reconstruct(t)
        out += t
    return out


NUMBERS = "0123456789"
OPENING_BRACKET = '['
CLOSING_BRACKET = ']'
