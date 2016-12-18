"""
# Primitive Types and Bitwise Operations

Binary operations are important to understand, because this is how numbers, characters
 and other primitives are represented in computer's memory.

For example, integer `6` in 8-bit binary representation is `110` or 0 • 2<sup>0</sup> + 1
 • 2<sup>1</sup> + 1 • 2<sup>2</sup>. Maximum value in 8-bit representation is
 2<sup>8</sup> - 1 or `255` or `1111 1111`. Modern languages use 16-, 32-bit integer
 type, such as `int` and `long` in C. Python 3 has unified `int` type which has no
 conventional bounds.

**Bitwise operators** (`&`, `|`, `^`, `~`, `>>`, `<<` ) operate on numbers treating
 them not as a single value, but as a string of bits.

**AND** operation (`&`) is used in **bit masking**. Masking to `1` allows to query bit's
 status, i.e. `5 & 1` is `1` (`0101 & 0001 = 0001`), in other words we verify that the
 least significant (rightmost) bit is set. Similarly, bit masking to `0` allows switching
 the bit off.

**XOR** is a logical operation that outputs true only when inputs differ (one is true, the
 other is false. Based on this definition, bitwise XOR-to-1 is commonly used for switching
 bit state, i.e. `5 ^ 15` is `10` (`0101 ^ 1111 = 1010`).

**Bit shifting** will shift all the bits in a word by arbitrary number of positions.
 Shifting *n* times is roughly the analog of multiplying (`<<`) or dividing (`>>`) the
 value by 2<sup>*n*</sup>. During left shift an unset bit is "shifted-in" at the least
 significant side. During right shift the least significant bit is discarded. For
 example, `5 >> 1 = 2` (`0101 >> 1 = 0010`).

Various combinations of these operations allow to quickly modify values in the memory.
"""


def count1(x):
    """
    Counts number of set bits in an integer word.

    The method uses the properties of bit masking to a single bit as well as bit shifting.

    Complexity: O(n), where n is the total number of bits in a word.
    :param int x: Input integer
    :return int: Number of set bits in an integer word
    """
    bits = 0
    while x:
        bits += x & 1
        x >>= 1
    return bits


def swap(a, b):
    """
    Swaps two integers in a tuple without using extra memory.

    Bitwise XOR sets the bits in the result to 1 if either, but not both, of the
     corresponding bits in the two operands is 1.

    Complexity: O(1), no extra space.
    :param int a: Input integer
    :param int b: Input integer
    :return tuple: Tuple of two swapped integers
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b
