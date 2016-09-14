# Merge Intervals

Given a list of intervals as tuples, where each tuple is two integers `(start, end)`, merge overlapping intervals:
```
Input: [(1, 3), (3, 6), (1, 5), (2, 4), (7, 8)]
0 [ - - - - - - - - - ] 10
    1---3       7---9
    1-------5
      2---4
        3-----6
Output: [(1, 6), (7, 8)]
```

###See code:
- [Solution](./__init__.py)
- [Test](./test.py)