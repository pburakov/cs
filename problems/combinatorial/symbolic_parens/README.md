# Symbolic Parentheses

Given a symbolic boolean expression containing `0`s (False), `1`s (True) and symbols `^`
 (XOR), `|` (OR) and `&` (AND), count in how many ways it can be parenthesized in order
 to evaluate to a given boolean.

Examples:
```
count_ways("1^0|0|1", False) -> 2
count_ways("0&0&0&1^1|0", True) -> 10
```

This problem is described in detail in Gayle McDowell's book "Cracking the Coding
 Interview".

###See code:
- [Solution](./__init__.py)
- [Test](./test.py)