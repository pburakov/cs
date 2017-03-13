"""
Dynamic Table
=============

Often we don't know in advance how many objects we need to store. We might want to
allocate additional space, which then has to be erased when it's no longer needed. Dynamic
table holds an array of **slots**, and it expands or contracts its allocated memory based
on the number of items in use.

Dynamic table best describes the concept of **amortized cost**. Reallocation operations
take linear time, but they happen only when the table reaches its critical constant **load
factor** :math:`\\alpha`. It guarantees that the unused space never exceed a constant
fraction of a total allocated space.

In this implementation we set :math:`\\alpha=1/2` for `insert` and :math:`\\alpha=1/4` for
`delete` operation (see method documentation). **Elementary insert/delete** operations
take :math:`O(1)` time. Since the amortized cost of each operation is bounded by a
constant, the actual time for any sequence of :math:`n` operations on a dynamic table is
:math:`O(n)`.

For a basic dynamic table, without an slot mapping function, no fast lookups are supported.
We assume that the dynamic table supports `insert` and `delete` operations. Each item
occupies a single slot and can be marked as erased (empty). Allocation table is represented
as Python lists.

"""


class DynamicTable:
    """Basic implementation of a dynamic table.
    """

    def __init__(self):
        self.table = [] * 0
        self.size = 0  # Total number of allocated slots
        self.num = 0  # Number of non-empty slots in the table
        self.used = 0  # Used slots (including marked as empty)

    def allocate(self, s):
        """Re-allocates a table of given size with existing elements.

        Allocates a new table. Carries un-deleted elements over from the old table then
        replaces old table with newly allocated version. Allocation is allowed only only
        if newly allocated table can hold of the current elements which were not marked as
        erased.

        Complexity:
            :math:`O(n)` where :math:`n` is the number of elements currently in the table.

        :param int s: New size, must be greater than the current amount of non-empty slots.

        """
        if s < self.num:
            raise MemoryError("Insufficient size to hold existing elements")
        new_table = [None] * s  # Allocating new table
        i = 0
        while i < self.used:
            if self.table[i] is not None:
                new_table[i] = self.table[i]
            i += 1
        self.used = i
        self.table = new_table
        self.size = s

    def insert(self, x):
        """Inserts an element into dynamic table.

        Increments related counters.

        Complexity:
            :math:`O(1)`.

        :param x: An element to insert.

        """
        i = self.used
        self.table[i] = x
        self.used += 1
        self.num += 1

    def erase(self, i):
        """Marks an element as erased.

        Complexity:
            :math:`O(1)`

        :param int i: Index of a table slot to erase.

        """
        if self.table[i] is not None:
            self.table[i] = None
            self.num -= 1


def table_insert(T, x):
    """Inserts an element into a dynamic table.

    The element is simply inserted into an existing array into a previously allocated
    slot. Once the table has approached its current limit of memory slots, it needs to be
    **expanded**. All the elements from an old table must be carried over to a new one. A
    common heuristic allocates a new table with twice as many slots.

    Complexity:
        :math:`O(1)` *amortized*. Elementary insertion, which statistically happens most
        of the time, has a constant cost.

    :param DynamicTable T: Dynamic table object.
    :param x: An object to insert.

    """
    if T.size == 0:
        T.allocate(1)
    if T.num == T.size:
        s = T.size * 2
        T.allocate(s)
    T.insert(x)


def table_delete(T, i):
    """Deletes an element from a dynamic table.

    This algorithm assumes the current index of an element is known.

    To implement a `delete` operation it is simple enough to remove the specified item
    from the table. In order to minimize the amount of wasted space, the table needs to be
    **contracted** once the "critical mass" of empty slots has been reached. This is done
    by a reallocation, analogous to `table insert`.

    It is possible that after expanding the table, we may not delete enough items to pay
    for a contraction, or otherwise, not insert enough items to pay for an expansion. In
    other words, we can find our table expanding and contracting too often when we're
    operating near the load factor bound.

    We can improve the loading strategy by allowing the load factor to drop below
    :math:`1/2`. We continue to double the table size upon inserting an item into a full
    table, but we halve the table size when deleting an item causes the table to become
    less than :math:`1/4` full.

    Complexity:
        :math:`O(1)` *amortized*. Elementary deletion, which statistically happens most of
        the time, has a constant cost.

    :param DynamicTable T: Dynamic table object.
    :param int i: Index of an element to delete.

    """
    if T.size == 0:
        raise ValueError("Table underflow")
    T.erase(i)
    if T.num <= T.size / 4:
        s = T.size // 2
        T.allocate(s)
