# Longes Common Substring

Longest Common Substring, or LCS (Longest Common Subsequence) is similar to many other 
 dynamic programming puzzles.

Given two strings, *X* and *Y*, find the longest string which is substring of both *X*
 and *Y*. The longest common substring of the strings `"BABCA"` and `"ABCBA"` is the
 string `"ABC"` of length 3.

The solution is based on Edit Distance solution routine, but returns an actual string.

###See code:
- [Solution (Recursive)](./__init__.py)
- [Solution (DP)](./__init__.py)
- [Solution (Length)](./__init__.py)
- [Test](./test.py)