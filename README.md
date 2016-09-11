# Algorithms and Data Structures

> Jump to [contents](#contents)

## Overview
Most companies measure candidate's skills by the ability to solve algorithmic problems 
 and his/her knowledge of data structures. 

Here you'll find implementations of most data structures and common algorithms a college 
 graduate should know. Implementations are accompanied by in-code comments and brief 
 essential information about them. 

The code is written in **Python 3**. Data structures are implemented as Python modules. 
 If you never used Python before, I strongly recommend to get familiar with its syntax 
 and modules, before starting.

The contents of this repository are not a replacement for Computer Science class. I 
 started working on this repository when I was preparing for interviews as I needed to 
 brush up on my CS skills. Solutions repository contains solutions of some common 
 problems that are encountered on interviews or set the pattern for their solution. 

## Sources
Most implementations are taken or adapted from the following books:
 * Thomas Cormen et al. Introduction To Algorithms (CLRS)
 * Steven Skiena. Algorithm Design Manual
 * Gyle McDowell. Cracking the Coding Interview
 * Adnan Aziz et al. Elements of Programming Interviews
 * Jon Bentley. Programming Pearls

I highly recommend to keep CLRS book as a reference, while carefully studying at least 
 one of the remaining books. The more practice you do, the better you perform, and 
 there's simply no other way around it.
 
Some solutions may contain ideas or code snippets from sites:
* [geeksforgeeks.com](http://www.geeksforgeeks.org)
* [rosettacode.org](https://rosettacode.org)
* [leetcode.com](https://leetcode.com)
* [stackoverflow.com](https://stackoverflow.com)

All of the above are great source of programming problems and their solutions.
 
## Usage Notes
I often use single-letter variables, because that is how they appear in the most 
 academic descriptions. Python comes very close to pseudo-code, often used in these 
 books. In my subjective opinion, such notation forces reader to deeply understanding 
 of an algorithm. 

Please note, that **all methods and classes have documentation** and a brief description
 of principle of their operation as well as notes on **their running time and space 
 complexity**.

If you feel uncomfortable understanding the code:
- read the description or function signature;
- try step-running an algorithm with your own test-case using debugger; 
- read up and re-write an algorithm using your own notation.

[PyCharm IDE](https://www.jetbrains.com/pycharm) is a great tool for all of those. I.e. 
 you can get information and navigate to the implementation by just hovering your mouse
 over a function or an object while holding `command` button (on Mac).

Also, all of the modules are ready for external use. You can reuse them in your 
 algorithms. Here's an example:
```
from trees.avl import Node
from trees.avl import AVLTree as Tree
from trees.avl import avl_insert
from trees.binary import in_order

my_tree = Tree()
avl_insert(my_tree, Node(3))
avl_insert(my_tree, Node(1))
avl_insert(my_tree, Node(2))
avl_insert(my_tree, Node(4))
in_order(my_tree.root, lambda x: print(x, end=' ')) 
# Prints "1 2 3 4 "
```
Modules are logically organized by the subject.

## Contents
* Basic Data Structures
  * [Linked List](/basic_data_structures/linked_list)
  * [Queue](/basic_data_structures/fifo)
  * [Stack](/basic_data_structures/lifo)
  * [Min/Max Heap](/basic_data_structures/heaps)
  * Dynamic Hash Map
* Trees
  * [Binary Tree](/trees/binary)
  * [Binary Search Tree](/trees/bst)
  * [AVL Tree](/trees/avl)
  * Red-Black Tree
* Sorting
  * Comparison
      * [Insertion Sort](/sorting/insertion_sort.py)
      * [Bubble Sort](/sorting/bubble_sort.py)
      * [Heap Sort](/sorting/heap_sort.py)
  * Divide-and-conquer
      * [Merge Sort](/sorting/merge_sort.py)
      * [Quicksort](/sorting/quicksort.py)
  * Counting Sort
      * [Bucket Sort](/sorting/bucket_sort.py)
      * [Counting Sort](/sorting/counting_sort.py)
      * [Radix Sort](/sorting/radix_sort.py)
* Numeric
  * [Base conversion](/numeric/__init__.py)
  * [Euclid's GCD Algorithm](/numeric/__init__.py)
* String Matching Algorithm
  * [Naive](/string_matching/naive.py)
  * [Knuth-Morris-Pratt](/string_matching/kmp.py)
  * [Rabin-Karp Running Hash](/string_matching/rabin_karp.py)
  * [Manacher's Palindrome Matching](/string_matching/manacher.py)
* [Graphs](/graphs)
  * [Graph Search Algorithms](/graphs/search)
  * [Topological Sort](/graphs/topological_sort)
  * [Shortest Paths Algorithms](/graphs/shortest_paths)
* Combinatorial Search
  * [Recursive Operations on Sets](/combinatorial/search)
  * [Optimization, Memoization, Dynamic Programming](/combinatorial/optimization)
* Appendix: [Solutions by Subject](/solutions)

## Disclaimer
This repository was created for personal use for the purpose of study. While I did my 
 best of proving correctness of those algorithms, I do not encourage production use of 
 any of these code snippets.