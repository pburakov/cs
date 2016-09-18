# Cut Rod

Imagine we have a rod and we can cut it to pieces of integral lengths. Each length has a
 price, and our task is to cut to get the maximum profit for any given length if possible.
 Given length may not exceed the maximum length we have in our "price-list".

Example:
 Given the price chart `P=[0, 1, 5, 8, 9]`, where `P[i]` is the profit for cut of length
 `i`, and a total length of `n=4`, the optimal strategy would be to make two cuts of
 length `2` which will result in maximum gain of `10` and not `9`.

This is an excellent example of evolution of a dynamic programming solution from a
 recursion. It is described in detail in CLRS book (Introduction to Algorithms).

###See code:
- [Solution (Recursive)](./__init__.py)
- [Solution (Memoized)](./__init__.py)
- [Solution (DP)](./__init__.py)
- [Test](./test.py)