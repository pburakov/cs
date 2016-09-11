# Dynamic Programming

Optimization problems can have many possible solutions, each of which has a value, and
 we wish to find one with the optimal (minimum or maximum) value. These problems are
 typically solved with the use of **dynamic programming** or DP.

There two key attributes that a problem must have in order for DP to be applicable:
 *overlapping sub-problems* and *optimal substructure*. DP usually involves the use of 
 some sort of *memoization* technique. Solutions are built on sub-problems that already 
 have been solved to optimality, or are being solved repeatedly.

DP solution is not obvious. Suggested first step is finding a recursive solution first.
 Second step is finding the state or the configuration that can be saved and reused. A
 helpful technique is describing state transitions as a graph problem to which a
 shortest or longest path algorithm can be applied. In fact Richard Bellman, one of the
 contributors to **Bellman-Ford** algorithm, was the one who developed the idea of 
 dynamic programming.

Some famous DP problems include: Knapsack, Rod Cutting, Edit Distance, Longest Common
 Subsequence, Longest Increasing Sequence, Coin Change, Matrix Multiplication, Text
 Justification, Max Cost Grid Path and many more. Some of them can be found in the
 [Solutions](/solutions) section.

Below are some basic DP templates, that help introducing the concept. It is essential to
 thoroughly examine these, including comments. Keep in mind, that practical applications
 of DP go well beyond these examples and require substantial amount of practice.