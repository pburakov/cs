import time

"""
Factorial is a product of all the whole numbers from 1 to n.

Example: 6! = 1*2*3*4*5*6 = 720

Just as in Fibonacci example, in this example recursive approach is not
 the most optimal, although it's not significant for reasonable integer value
 of n. factorial_recursive() is O(n^2) while factorial() is O(n).
"""


def factorial_recursive(n):
    if n > 0:
        return n * factorial_recursive(n - 1)
    else:
        return 1


start_time = time.clock()
print(factorial_recursive(1000))
print("recursion time: %6.6f" % (time.clock() - start_time))


def factorial(n):
    out = 1
    for i in range(1, n + 1):
        out *= i
    return out


start_time = time.clock()
print(factorial(1000))
print("iteration time: %6.6f" % (time.clock() - start_time))
