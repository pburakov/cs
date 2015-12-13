import time

"""
These two methods return the n-th number in a Fibonacci sequence, where
 n-th number is the sum of F(n-2) + F(n-1).

Fibonacci sequence (F):
 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...

This sequence is a perfect example although it is given in a recursive form,
 recursive algorithmic solution is not the most optimal. The complexity of F_rec()
 is O(n^2), while iterative function F() is a simple O(n).
"""


def F(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(F(25))
start_time = time.clock()
print("iteration time: %6.6f" % (time.clock() - start_time))


def F_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F_rec(n - 1) + F_rec(n - 2)


start_time = time.clock()
print(F_rec(25))
print("recursive time: %6.6f" % (time.clock() - start_time))
