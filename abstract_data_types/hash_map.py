class HashMap:
    """
    Basic implementation of a Hash Table with integer keys.

    Hash function formula:
     Hash = Key % MapSize.

    Therefore:
     Hash is integer.
     0 < Hash < MapSize

    Hash collision is resolved using rehashing formula
     NewHash = (OldHash + 1) % MapSize
    until an empty slot is found. This method is called linear probing.

    This implementation is very basic and is for demonstration purposes only.
     The bigger HashMap gets, the more collisions will occur and the cost of put()
     and get() methods will rise to O(n).
    """

    def __init__(self, size):
        self.size = int(size)
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash(self, key):
        return int(key) % self.size

    def rehash(self, old_hash):
        return (int(old_hash) + 1) % self.size

    def put(self, key, value):
        hash_i = self.hash(key)
        if self.slots[hash_i] is None:
            self.slots[hash_i] = key
            self.data[hash_i] = value
        else:
            if self.slots[hash_i] == key:
                self.data[hash_i] = value
            else:
                next_i = self.rehash(hash_i)
                while self.slots[next_i] and self.slots[next_i] != key:
                    next_i = self.rehash(next_i)
                if self.slots[next_i] is None:
                    self.slots[next_i] = key
                    self.data[next_i] = value
                else:
                    self.data[next_i] = value

    def get(self, key):
        hash_i = self.hash(key)
        next_i = hash_i
        while self.slots[next_i]:
            if self.slots[next_i] == key:
                return self.data[next_i]
            else:
                next_i = self.rehash(next_i)
                if next_i == hash_i:
                    return None


hash_table = HashMap(6)
hash_table.put(36, 'dog')
hash_table.put(6, 'cat')
hash_table.put(24, 'duck')
hash_table.put(5, 'giraffe')
hash_table.put(42, 'weasel')
hash_table.put(30, 'lion')
print(hash_table.slots)
print(hash_table.data)
print(hash_table.get(30))
