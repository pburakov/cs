"""
Bitwise Operations
==================

Bit-level operations are essential, since data primitives are presented and operated in the
computer's memory using bits. For example, integer :math:`6` can be represented as 8-bit
word ``0000 0110``. Each register represents whether the next power of :math:`2` should be
added to the total value, counting from right (:math:`2^0`) to left (:math:`2^8`). Maximum
value in 8-bit representation is :math:`2^8 - 1 = 255` or ``1111 1111``. Modern languages
use 32- and 64-bit integer type, such as ``int`` and ``long`` in Java. Python 3 has a
unified ``int`` type which has no conventional bounds.

Bitwise operators (``&``, ``|``, ``^``, ``~``, ``>>``, ``<<`` ) operate on numbers treating
them not as a single value, but as a string of bits.

AND operation (``&``) is used in **bit masking**. Masking to 1 allows to query bit's
status, i.e. ``5 & 1 = 1`` (``0101 & 0001 = 0001``). In other words we can verify that the
least significant bit (rightmost bit representing least power of 2, **LSB** for short) is
set. Bit masking to 0 allows switching the bit off.

XOR is a logical operation that outputs true only when the inputs differ (one is true, the
other is false). Based on this definition, bitwise XOR-to-1 is commonly used for switching
bit state, i.e. ``5 ^ 15 = 10`` (``0101 ^ 1111 = 1010``).

**Bit shifting** will shift all the bits in a word one position at a time. Shifting *n*
times is roughly the analog of multiplying (``<<``) or dividing (``>>``) the value by
:math:`2^n`. During left shift, an unset (`0`) bit is "shifted-in" at the least significant
side. During right shift the least significant bit is discarded. For example, ``5 >> 1 = 2``
(``0101 >> 1 = 0010``).

Various combinations of these operations allow to quickly modify values in the memory.
"""


def count1(x):
    """Counts number of set bits in an integer word.

    The method repeatedly shifts the word, then counts the least significant bit, if it is
    set to ``1``, using bit masking.

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
    """Computes parity of a binary word.

    Parity is 1 if a number of set bits in a binary word is odd.

    Parity checks are used to detect single-bit errors in a data stream or a storage.

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
