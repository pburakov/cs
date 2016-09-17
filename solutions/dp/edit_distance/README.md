# Edit Distance

In computer science, edit distance (**Levenstein** distance) is a way of quantifying how
 dissimilar two strings are to one another by counting the minimum number of operations
 required to transform one string into the other.

You are given a source string *S* and a target string *T*. Three types of operations are
 possible, let `1` be the equal cost of each:
 - **replace** (substitute) character in string *S* with a character from string *T*.
 - **insert** a character into string *S* to help it match string *T*.
 - **delete** a character from string *S*.

Find minimum amount of edits required to transform *S* into *T*. For example, edit
 distance of string "cat" and "nuts" is 3 (add `s`, replace `a` with `u`, replace `c`
 with `n`).

This algorithm is used in spell checkers and to quantify the similarity of DNA
 sequences. It is described in great detail in the book "Algorithm Design Manual" by
 S. Skiena.

###See code:
- [Solution (Recursive)](./__init__.py)
- [Solution (DP)](./__init__.py)
- [Test](./test.py)