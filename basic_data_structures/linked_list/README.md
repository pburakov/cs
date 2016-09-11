# Linked List

Linked list is a simple data structure in which the objects are arranged in a linear
 order. Unlike an array, however, in which elements are ordered by the array indices,
 linked list is ordered using pointers in each object. Linked list provides a
 simple, flexible, although not very efficient, representation for dynamic sets.

Every node of a basic linked list holds some data, called the key and a reference to
 the next element. Last element of the singly linked list points to a null object. Head
 of the list points to a first object in the list. In order to find an element with a
 given key, the list has to be searched starting at the head.

There are various kinds of linked lists. For instance, the last element of a **circular
 list** has no null pointer. Instead it points to the head element, effectively making
 a loop. Ordered linked lists offer certain advantages in searching, but increase
 the cost for inserting. This is an implementation of a **doubly linked** list where 
 every element additionally holds a reference to a previous element.

Please note, that Python list is not implemented as a linked list. Internally Python
 lists are dynamic arrays (implemented as a vector of pointers).