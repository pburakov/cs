from threading import Lock
from basic_data_structures.linked_list import *

class HashMap:
    def __init__(self, n):
        if n <= 0:
            raise ValueError("Invalid size")
        self.items = [LinkedList() for _ in range(n)]
        self.size = 0
        self.locks = [Lock() for _ in range(n)]

    def __len__(self):
        return self.size

    def _hash(self, k):
        n = len(self.items)
        return hash(k) % n

    def put(self, k, x):
        i = self._hash(k)
        new_node = Node(k)
        new_node.value = x
        existing_node = list_search(self.items[i], k)
        if existing_node:
            list_delete(self.items[i], existing_node)
            self.size -= 1
        list_insert(self.items[i], new_node)
        self.size += 1

    def delete(self, k):
        i = self._hash(k)
        existing_node = list_search(self.items[i], k)
        if existing_node:
            list_delete(self.items[i], existing_node)
            self.size -= 1
        else:
            raise KeyError("No such key")

    def get(self, k):
        i = self._hash(k)
        existing_node = list_search(self.items[i], k)
        if existing_node:
            return existing_node.value
        else:
            raise KeyError("No such key")


h1 = HashMap(5)
h1.put('z', 0)
h1.put('a', 1)
h1.put('b', 2)
h1.put('c', 3)
h1.put('d', 4)
h1.put('e', 5)
h1.put('f', 6)
h1.put('g', 7)
h1.put('h', 8)
h1.put('i', 9)
h1.put('j', 10)
h1.put('k', 11)
h1.delete('d')
print(h1.get('f'))
print(h1.get('k'))
