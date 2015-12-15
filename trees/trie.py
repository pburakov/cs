class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        self.rec_insert(word, self.root)

    def rec_insert(self, word, node):
        if word[:1] not in node.pointers:
            new_node = Node()
            new_node.val = word[:1]
            node.pointers[word[:1]] = new_node
            self.rec_insert(word, node)
        else:
            next_node = node.pointers[word[:1]]
            if len(word[1:]) == 0:
                next_node.pointers[' '] = '__end__'
                return
            else:
                return self.rec_insert(word[1:], next_node)

    def search(self, word):
        if len(word) == 0:
            return False
        else:
            return self.rec_search(word, self.root)

    def rec_search(self, word, node):
        if word[:1] not in node.pointers:
            return False
        else:
            next_node = node.pointers[word[:1]]
            if len(word[1:]) == 0:
                if ' ' in next_node.pointers:
                    return True
                else:
                    return False
            else:
                return self.rec_search(word[1:], next_node)

    def starts_with(self, prefix):
        if len(prefix) == 0:
            return True
        else:
            self.rec_search_prefix(prefix, self.root)

    def rec_search_prefix(self, word, node):
        if word[:1] not in node.pointers:
            return False
        else:
            if len(word[1:]) == 0:
                return True
            next_node = node.pointers[word[:1]]
            return self.rec_search_prefix(word[1:], next_node)


class Node:
    def __init__(self):
        self.val = None
        self.pointers = {}


def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict['__end__'] = '__end__'
    return root


def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    else:
        if '__end__' in current_dict:
            return True
        else:
            return False


trie = make_trie('foo', 'foos')
print(trie)
print(in_trie(trie, 'foo'))
print(in_trie(trie, 'fo'))

trie_obj = Trie()
trie_obj.insert('foo')
trie_obj.insert('foos')
print(trie_obj.search('fooz'))
print(trie_obj.search('foos'))
print(trie_obj.starts_with('fo'))
