def gcd(a, b):
    """
     Returns GCD (greatest common divisor) for integers a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(12, 16))
print(gcd(3, 7))
print(gcd(5800, 130))
