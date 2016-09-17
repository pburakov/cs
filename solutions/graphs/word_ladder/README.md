# Word Ladder

This is a word production sequence problem, better known as word ladder. It can be found
 in many different flavours. Although it involves strings, it is a great example how
 simple graph algorithms can be used to solve various seemingly unrelated problems.

You are given a dictionary of words of the same lengths, consisting of lowercase letters. 
 Given a starting word and a target word, find the shortest available transformation 
 sequence, if such exists. Two rules have to be maintained:
  - at each step only a single letter can be changed at a time,
  - every word in a sequence must exist in a dictionary.

Example: 
```
D = {"hot","hit","dot","dog","cog","lot","log"} 
Output: "hit" -> "hot" -> "dot" -> "dog" -> "cog" (length: 5)
```

###See code:
- [Solution](./__init__.py)
- [Test](./test.py)