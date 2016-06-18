"""
Recursive solutions are built off of solutions to sub-problems.

Recursion sub-problem includes "base case", a solution for lowest argument
 or most trivial problem. Recursive algorithm should call itself while moving
 towards this base case.

There are many ways to divide big problems into sub-problem, often called
 bottom-up, top-down approach and half-and-half.

As memory stack increases for every recursive call, sometime recursive approach
 is used together with help of dynamic programming or memoization.

It's important to note that all recursive algorithms can be implemented
 iteratively. Recursive approach is preferred because iterative code
 is much more complex and most times is far less obvious.
"""


def all_n(n):
    if n == 1:
        return "1"
    else:
        return str(all_n(n - 1)) + " " + str(n)


def all_range_n(a, b):
    if a == b:
        return str(a)
    elif b > a:
        return str(all_range_n(a, b - 1)) + " " + str(b)
    elif b < a:
        return str(a) + " " + str(all_range_n(a - 1, b))


def akkerman(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akkerman(m - 1, 1)
    else:
        return akkerman(m - 1, akkerman(m, n - 1))


def is_base2(x):
    if x == 2:
        return True
    elif 1 <= x < 2:
        return False
    return is_base2(x / 2.0)


def digit_sum(x):
    if x < 1:
        return 0
    elif x < 10:
        return x
    else:
        return x % 10 + digit_sum(int(x / 10))
