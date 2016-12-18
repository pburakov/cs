"""
Bitwise Operations
==================

Bit-level operations are essential, since this is how data primitives are presented and
operated in computer's memory.

For example, integer 6 in 8-bit binary representation is ``0000 0110``. Each register
represent whether the next power of 2 should be added to the total value, counting from
right (:math:`2^0`) to left (:math:`2^8`).

Maximum value in 8-bit representation is :math:`2^8 - 1 = 255` or ``1111 1111``. Modern
languages use 16-, 32-bit integer type, such as ``int`` and ``long`` in C. Python 3 has
unified ``int`` type which has no conventional bounds.

Bitwise operators (``&``, ``|``, ``^``, ``~``, ``>>``, ``<<`` ) operate on numbers treating
them not as a single value, but as a string of bits.

AND operation (``&``) is used in **bit masking**. Masking to 1 allows to query bit's
status, i.e. ``5 & 1 = 1`` (``0101 & 0001 = 0001``), in other words we verify that the
least significant bit (rightmost bit representing least power of 2, **LSB** for short) is
set. Similarly, bit masking to 0 allows switching the bit off.

XOR is a logical operation that outputs true only when inputs differ (one is true, the
other is false). Based on this definition, bitwise XOR-to-1 is commonly used for switching
bit state, i.e. ``5 ^ 15 = 10`` (``0101 ^ 1111 = 1010``).

**Bit shifting** will shift all the bits in a word by arbitrary number of positions.
Shifting *n* times is roughly the analog of multiplying (``<<``) or dividing (``>>``) the
value by :math:`2^n`. During left shift an unset bit is "shifted-in" at the least
significant side. During right shift the least significant bit is discarded. For example,
``5 >> 1 = 2`` (``0101 >> 1 = 0010``).

Various combinations of these operations allow to quickly modify values in the memory.
"""


def count1(x):
    """Counts number of set bits in an integer word.

    The method uses the properties of bit masking to a single bit as well as bit shifting.

    Complexity:
        :math:`O(n)`, where :math:`n` is the total number of bits in a word.

    :param int x: Input integer.
    :return: Number of set bits in a binary integer word.

    """
    bits = 0
    while x:
        bits += x & 1
        x >>= 1
    return bits


def parity(x):
    """Returns parity of a binary word.

    Parity is 1 if a number of set bits in a binary word is odd. Parity checks are used
     to detect single-bit errors in data stream or storage.

    Complexity:
        :math:`O(n)`, where :math:`n` is number of bits in a word.

    :param int x: Input integer.
    :return: Parity of an input integer, 1 or 0.

    """
    p = 0
    while x:
        p ^= x & 1  # Switch `p` if LSB is different from previously saved `p`
        x >>= 1
    return p


def swap(a, b):
    """Swaps two integers in a tuple without using extra memory.

    This algorithm is based on properties of XOR operation. Binary values are "flipped"
     twice against each other.

    Complexity:
        :math:`O(1)`, no extra space.

    :param int a: Input integer
    :param int b: Input integer
    :return: Tuple of two swapped integers

    """
    a ^= b
    b ^= a
    a ^= b
    return a, b
