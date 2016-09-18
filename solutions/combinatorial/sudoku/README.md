# Sudoku Solver

A standard Sudoku puzzle contains 81 cells, in a 9 by 9 grid, and has 9 zones, each zone
 being the intersection of the first, middle, or last 3 rows, and the first, middle, or
 last 3 columns. Each cell may contain a number from one to nine; each number can only
 occur once in each zone, row, and column of the grid. Pre-filled cells are provided as
 clues.

Sudoku puzzle board is represented by two-dimensonal array of integers of size `9x9`.

Example input:
```
[
     [5, 3, 0, 0, 7, 0, 0, 0, 0],
     [6, 0, 0, 1, 9, 5, 0, 0, 0],
     [0, 9, 0, 0, 0, 0, 0, 6, 0],
     [8, 0, 0, 0, 6, 0, 0, 0, 3],
     [4, 0, 0, 8, 0, 3, 0, 0, 1],
     [7, 0, 0, 0, 2, 0, 0, 0, 6],
     [0, 6, 0, 0, 0, 0, 2, 8, 0],
     [0, 0, 0, 4, 1, 9, 0, 0, 5],
     [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

###See code:
- [Solution](./__init__.py)
- [Driver](./driver.py)