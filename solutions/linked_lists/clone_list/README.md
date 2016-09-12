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
When solving this problem (an other linked-list related problems), make sure to draw out
 the solution on paper or a whiteboard first, since it's very easy to lose track of
 pointer operations.

###See code:
- [Solution](/solutions/linked_lists/clone_list/__init__.py)
- [Test](/solutions/linked_lists/clone_list/test.py)