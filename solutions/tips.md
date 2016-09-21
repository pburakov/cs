# Interviewing Tips and Reminders

Read these before the interview or while studying.

##General
1. Don’t rush!
2. If it’s a phone screen take **notepad and pen**! On-site, you can re-write problem statement on a whiteboard. Even if repeated, it may help you figure out a solution as you write it.
3. Make sure you’re implementing the right solution before coding.
4. Ask for **desired running time**, especially when dealing with inexperienced interviewers. They may look for a specific solution.
5. See tip #1 again.
6. Start with writing a few simple **test cases** for yourself and see what the output for those would be.
7. Sometimes a problem statement can be a derivative of the problem that you already know, but solved completely different. See tip #1 again.
8. As a consequence of #7, **treat each problem like a completely new one**, even if you know it. It's ok to say something like *"I’m familiar with this problem, but let me prepare some more test cases"*, or *"Let me think of a better algorithm"*.
9. Be confident! Solving a problem should be exciting.

## Inexperienced Interviewers
Inexperienced interviewer may unconsciously try to intimidate you. They will try to steer your interview towards a solution they know, especially if they use a handbook or never solved the problem themselves. 

Don't let them lead too much, but be gentle about it. Ask questions, like *"What would be the key in a hash map you're suggesting?"* or *"How would you implement recursion in this case?"* Don't feel bad. My rule is that, if they perform interviewing process unprofessionally or unfriendly, it's most likely an environment you don't want to be in anyway.

## Numerical and Bit Ops
- Essential things to remember: modulo operation, Euclid’s GCD algorithm, base conversion, bit-shift, `XOR` (not to mention `AND` and `OR`).
- Reason about time complexity in pseudo-polynomial time (bound to number of digits or other sub-property).

## Linked Lists
- Directly stated LL-related problems almost always solved with one, two or more walking pointers. These types of questions unfortunately rely on some sort of a trick (which might, and should, be given to you as a hint).
- Also, lists occur in many problems as a sole data structure, or as an auxiliary data structure.
- **LRU cache** includes a combination of a linked list and a hash map.
- Most non-*O(n)* LL-algorithms trade running time for additional space and use auxiliary data structures: frequency maps, hash maps, stacks and queues.
- Edge cases and pointers are everything. Maintain focus, especially when implementing swapping and deleting!

## Stacks and Queues
- Feel free to combine stacks, two stacks, stack and queue and so on (see **Queue of Two Stacks** problem).
- If implementing one of these yourself (or any API in general in that sense), make sure the requirements are strongly defined! Make sure to get this information from the interviewer, before you begin.

## Arrays
- Solving array questions in linear time? Array can be traversed multiple times when needed. It will still be linear, if no nested loops.
- Many problems are solved with **rolling window** technique, a sum or a product of it.
- Try to measure if LIFO / FIFO / Heap can be applied.
- Also, fancy **bit ops** can be applied to array of integers.
- Too many `if` statements in a traversal? There may be a recursive solution.

## Strings
- In simple string problems, string is a fancy array, so same principles apply.
- Parsing strings? Think **finite state automata**, **recursion** and **DP**.
- If reasoning out the solution is getting too hard, you're probably on a wrong track.

## Vectors, Hash Sets and Hash Maps
- Don’t think Python lists (vectors) are magical. Slicing and arbitrary insertion still takes *O(k)* time (*k* being number of elements you want to skip).
- Dynamic Tables use **amortized time complexity**. Insert/delete/lookup times are *O(1)*, but should be mentioned that it’s amortized time. 

## Sorting
- You just have to remember the algorithms and their running times.
- Always feel free to use **built-in function** for sorting, and reason verbally about the sorting algorithm you would use.
- Lower bound for comparison sorting: *O(n log(n))*, only bucketing / counting sort allows linear time.
- A lot of solutions involve partitioning routine (smaller to the left, larger to the right) of **quicksort**. It's a most commonly encountered algorithm when comes to sorting.
- A lot of solutions involve merging routine (compare values at two pointers) of **merge sort**.

## Heaps
- Remember Heap rep invariant, and watch when it is maintained and when it is broken.
- Heaps pop up in random solutions. Two heaps are used in a **Median in a Stream of Integers** problem. It can be hard to come up with.

## Trees and BST
- Most binary tree solutions evolve around in-order, pre-order and post-order traversal. 
- Recursion is essential, unless iteration was asked explicitly. **Iteration** recreates recursive algorithm using structures like **queue** and **stack**.
- For **level order** traversal (for printing or creating lists of nodes) use BST with node counters.
- Remember BST properties, and watch when they are maintained and when they are broken. Examples: finding **Lowest Common Ancestor** or **BST rotation**.
- Don't confuse regular binary tree with BST or B-Tree.

## Combinatorial and n-choose-k
- Learn recursive algorithms for permutations, subsets and partitions, the logic is very similar.
- If you're stuck - try drawing a recursion tree.
- Recursive recipes for permutations: permutations - swapping, partitioning - splitting, subsets - picking.
- Combinatorial problems are usually bounded by the output: *n!* permutations, *2<sup>n/2</sup>* partitions, *2<sup>n</sup>* subsets.

## Graphs
- Reason about graphs. DFS and BFS are essential and applied in 70% of the cases.
- Graph algorithms can be applied to matrices, arrays, lists.
- Try to draw a simple, 1D, topologically sorted DAG, if it can be applied. Example: snakes and ladders board.
- DFS is stack (or recursive stack), BFS - queue, path algorithms - DP.
- Learn how to implement some fancy search algorithm like A* (Dijkstra with heuristic), just for fun.

## Dynamic Programming
- One of the hardest topics, but very rewarding once mastered.
- Lay it down as a graph (MIT does it), start with recursion, find out the recursive formula.
- Most often formula for 1-dimensional state storage looks like `DP[i] = DP[i-1] + foo(x)`. More often this formula has two or more conditionals.
- Be careful with the code, it gets messy with indexes and keeping the state.

