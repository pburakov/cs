# Stack

Stack is a dynamic set that follows **"last-in, first-out"** policy. This means that the
 element deleted from the set is the one most recently inserted.

Stack can be implemented using a linked list where the head of the list is also the top of
 the stack .

This implementation uses an array of size *n* to store the elements and guarantee *O(1)*
 time for LIFO operations. *n* is the maximum amount of elements that the stack can hold.
 Elements are never physically removed from the array. It's only the pointer to the top of
 the stack, represented by an array index, that is updated. This pointer keeps elements
 that are still used in the stack from being replaced by newly added elements.

The removed element is always at the top of the stack.

###See code: 
- [Stack](/basic_data_structures/lifo/__init__.py)