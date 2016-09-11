# Combinatorial Search

Many combinatorial search problems can be solved to optimality using exhaustive search
 techniques, although computational cost of such solutions can be enormous, even
 unfeasible. Time and space complexity of such problems are coherent with the size of
 its output. It can be predicted using counting theory formulas.

This type of problems is often called **"n-choose-k"**, due to the binomial coefficient
 that denotes the number of *k*-combinations of a set of *n* elements.

Combinatorial search algorithms use recursion with a **backtracking** technique. 
 Recursive solutions resemble depth-first search algorithm where graph represents all 
 possible configurations, or states. Backtracking is a systematic way to iterate 
 through all the sates in a search space, while avoiding repetitions and bad 
 configurations. Backtracking algorithm abandons a partial candidate as soon as it 
 determines that it cannot possibly lead to a valid solution

Description of common steps of a backtracking algorithm:
 1. Define base case for recursion to finish. For instance, report a found solution or
  report that algorithm has exhausted all possible solutions for given configuration.
 2. Construct a new candidate, or several, for a solution. For example, exclude, swap
  or replace an element of a set.
 3. Check if proposed solution does not violate problem conditions. This is where we
  abandon a branch of a recursive tree (not shown in examples).
 4. Call itself on new candidate or, if there are many, on each of the new candidates.
 5. Undo updates made to a set (optional). This step occurs after the running process
  exits the recursion (or "backtracks").

This module contains implementation templates and techniques for some of the most 
 common combinatorial search problems.

###See code: 
- [Recursive Operations on Sets](/combinatorial/search/__init__.py)