# Queue

Queue is a dynamic set that follows "first-in, first-out" policy. This means that the
 element deleted from the set is the one that have been in the queue for the longest
 time.

Queue can be implemented using a doubly linked list using pointers to the head and
 the tail of the list as the head and the tail of the queue.

This implementation uses an array of size *n* to store the elements. *n* is the
 maximum amount of elements that the queue can hold. Elements are never physically
 removed from the array. Only pointers to the head and the tail of the queue,
 represented by array indices, are shifted. Pointers keep elements that are still
 used in the queue from being replaced by newly added elements.

Keeping track of a quantity of currently enqueued elements helps making sure that
 the allocated size is never exceeded. In some sense, this representation of a queue
 resembles a snake chasing its own tail.

Like a newly arriving customer takes a place in the line, the enqueued element is
 added at the tail of the queue. And like the customer at the head of the line, the
 de-queued element is always at the head of a queue.
