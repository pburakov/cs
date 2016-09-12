from solutions.linked_lists.clone_list import *

l1 = List()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
e.other = c
d.other = a
l1.insert(e)
l1.insert(d)
l1.insert(c)
l1.insert(b)
l1.insert(a)
print(l1)
l2 = clone(l1)
print(l2)
