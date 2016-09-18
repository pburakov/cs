# Knapsack Problem

Knapsack problem is similar to a Rod Cutting problem, It is another example of a common
 approach, seen in Dynamic Programming.

Imagine you have a list of items, each has an associated value and weight. You are also
 given a bag of a limited capacity (maximum weight it can hold). Your task is to maximise
 the value of items a bag can hold.

Example:
```
    Item Value Weight
      a    60    5          Bag capacity = 5.
      b    50    3
      c    70    4          Answer: 80 (items b and d).
      d    30    2
```

This problem is described in detail in the book "Elements of Programming Interviews" by
 A. Aziz et al.

###See code:
- [Solution (Recursive)](./__init__.py)
- [Solution (DP)](./__init__.py)
- [Test](./test.py)