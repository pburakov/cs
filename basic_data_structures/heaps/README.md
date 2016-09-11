# Heaps

Binary heap is a basic implementation of a **priority queue**. Although heap is presented
 as a binary tree, is is usually implemented as an array (or a list in Python) because 
 the tree representation of a heap is nearly complete.

Given that the first index of a tree starts at `0`, the index of a child node in an array
 representation can be computed as `i * 2 + 1` for left side child and `i * 2 + 2` for 
 right side child.

Representation invariant of a binary heap determines its main use and common variations:
 **max-heap** and **min-heap**. For max-heap, every element is bigger than its children
 (vise versa for min heap). Thus, by induction, it can be proven that the largest (or 
 smallest in case of min-heap) element will always be on the top as long as heap
 properties are maintained at any modification made to its structure.

Heap structure is useful when a fast *O(n)* access to the top element is required.
 However, the remainder of the array is kept partially unsorted. Heaps are commonly in 
 various algorithms. This heap implementation contains various additional properties, that
 help reducing running times in various cases.
 
###See code: 
- [Min-heap](/min_heap.py)
- [Max-heap](/min_heap.py)