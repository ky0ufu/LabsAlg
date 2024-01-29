class TrieNode:
    def __init__(self):
        self.children = {}
        self.start = -1  # Начальная позиция суффикса в тексте
        self.end = -1    # Конечная позиция суффикса в тексте
        self.suffix_link = None

class SuffixTrie:
    def __init__(self, text):
        self.root = TrieNode()
        self.text = text
        self.build_suffix_trie(text)
        self.build_suffix_links()

    def build_suffix_trie(self, text):
        for i in range(len(text)):
            current_node = self.root
            for j in range(i, len(text)):
                char = text[j]
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]
            current_node.start = i
            current_node.end = len(text) - 1

    def build_suffix_links(self):
        queue = [self.root]

        while queue:
            current_node = queue.pop(0)

            for key, child_node in current_node.children.items():
                queue.append(child_node)

                if current_node == self.root:
                    child_node.suffix_link = self.root
                else:
                    suffix_link_node = current_node.suffix_link

                    while suffix_link_node and key not in suffix_link_node.children:
                        suffix_link_node = suffix_link_node.suffix_link

                    if suffix_link_node:
                        child_node.suffix_link = suffix_link_node.children[key]
                    else:
                        child_node.suffix_link = self.root

    def find_suffix_position(self, suffix):
        current_node = self.root
        for char in suffix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]

        return current_node.start if current_node else None

    def print_suffixes(self):
        self._print_suffixes(self.root, "")

    def _print_suffixes(self, node, suffix):
        for key, child_node in node.children.items():
            new_suffix = suffix + key
            print(f"Suffix: {new_suffix}, Position: {child_node.start}")
            self._print_suffixes(child_node, new_suffix)


text = "bananaapplepan"
suffix_trie = SuffixTrie(text)

#suffix_trie.print_suffixes()

suffix_to_find = "lepan"
position = suffix_trie.find_suffix_position(suffix_to_find)

if position is not None:
    print(f"The position of the suffix {suffix_to_find} is {position}")
else:
    print(f"The suffix {suffix_to_find} is not found.")