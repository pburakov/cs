from abstract_data_types.stack import Stack

digits = "0123456789ABCDEF"


def base_convert(decimal_num, base):
    """
    Converts decimal number into any base [that can be printed
    using 0-9A-F chars] using Stack
    """

    stack = Stack()
    while decimal_num > 0:
        remainder = decimal_num % base
        stack.add(remainder)
        decimal_num = decimal_num // base

    output = ''
    while not stack.is_empty():
        output += digits[stack.pop()]

    return output


def base_recursive(n, base):
    """
    Recursive implementation of the same algorithm.
    To understand, start with the base case of base_recursive(1, 2)
    """
    if n < base:
        return digits[n]
    else:
        return base_recursive(n // base, base) + digits[n % base]


print(base_convert(6, 2))  # Binary (110)
print(base_convert(128, 8))  # Octal (200)
print(base_convert(123, 16))  # Hex (7B)
print(base_convert(2056, 13))  # Base 13 (C22)

print(base_recursive(6, 2))  # Binary (110)
print(base_recursive(128, 8))  # Octal (200)
print(base_recursive(123, 16))  # Hex (7B)
print(base_recursive(2056, 13))  # Base 13 (C22)
