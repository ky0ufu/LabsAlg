class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def is_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


trie = Trie()
words = ["apple", "app", "apricot", "banana"]
for word in words:
    trie.insert(word)

print(trie.search("apple"))
print(trie.search("app"))
print(trie.search("apricot"))
print(trie.search("ban"))

print(trie.is_prefix("ap"))
print(trie.is_prefix("ba"))
print(trie.is_prefix("foo"))