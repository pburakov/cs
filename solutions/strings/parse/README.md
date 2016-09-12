# Parse Syntax

Given a simple syntax, using numbers and square brackets, parse a given expression into a
 complete string. Numbers specify how many times following character or expression shall
 be repeated. Default number of repetitions of a character or an expression is 1, unless
 explicitly specified. Nested expressions are enclosed in square brackets.

Examples:
```
Input: "ab4c". Output: "abcccc"
Input: "ab0c". Output: "ab"
Input: "2[a2bc]". Output: "abbcabbc"
Input: "2[ab3[cd]]x3yz". Output: "abcdcdcdabcdcdcdxyyyz"
```
I've been asked this problem when I was interviewing with Google. Here is my stab at it.

###See code:
- [Solution](/solutions/strings/parse_syntax/__init__.py)
- [Test](/solutions/strings/parse_syntax/test.py)
