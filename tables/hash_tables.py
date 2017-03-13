"""
Hash Tables
===========

Hash Table is a dynamic set that supports dictionary operations `insert`, `search` and
`delete`. Hash tables can be of fixed size, or be dynamic and share properties of amortized
analysis of a dynamic table. In Python hash tables are dynamic and are defined as `dict`
type.

The data-structure under the hood of a hash table is an array. As we know, directly
addressing the value in an array takes :math:`O(1)` if we know the slot index. We can
generalize this notion and use a **hash function** :math:`h`. The better the function
uniformity is, the less likely collisions is to occur, and the better is the performance of
a hash table.

Our hash table needs an effective way to resolve collisions, when more than one key maps to
same array index. There are several ways to minimize the effect of collisions such as
`chaining` and `open addressing`. These methods denote different flavors of hash tables.

"""
from tables.dynamic import DynamicTable


class HashTable(DynamicTable):
    pass
