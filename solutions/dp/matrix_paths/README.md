# Paths in Matrix

Given a 2-D array sized *m*x*n*, find number of ways to get from the top left corner to the bottom right corner by moving strictly right or down. Cells with a value of `1` cannot be traversed.

Example
```
Input: [
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 0]
]
Output: 4
```

This is a combinatorial problem that has the necessary properties for a dynamic programming solution. 