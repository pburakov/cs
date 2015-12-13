from abstract_data_types.hash_map import HashMap

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
