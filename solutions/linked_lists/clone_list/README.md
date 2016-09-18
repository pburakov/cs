# Clone List with Arbitrary Pointer 

Given singly linked list consisting of elements that have a second pointer pointing to an
 arbitrary node in the same list, write an efficient function to deeply clone it.

Node structure for reference:
```
template<typename T>
struct Node {
    T key;
    Node *other;
    Node *next;
};
```

###See code:
- [Solution](./__init__.py)
- [Test](./test.py)