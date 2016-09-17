# Longes Common Substring

Longest Common Substring, or LCS (Longest Common
 Subsequence) is similar to many other dynamic programming puzzles.

Given two strings, *X* and *Y*, find the longest string which is substring of both *X*
 and *Y*. The longest common substring of the strings `"BABCA"` and `"ABCBA"` is
 string `"ABC"` of length 3. Other common substrings are `"A"`, `"AB"`, `"B"`, `"BA"`, `"BC"` and
 `"C"`.

The solution is based on Edit Distance solution routine, but returns an actual string.
