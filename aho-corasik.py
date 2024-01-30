class TrieNode:
    def __init__(self):
        self.children = {}
        self.link = None
        self.words_in_node = []


def build_trie(words):
    root = TrieNode()

    for word in words:
        node = root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.words_in_node.append(word)

    return root


def build_link_transitions(root):
    queue = []
    for node in root.children.values():
        queue.append(node)
        node.link = root

    while queue:
        current_node = queue.pop(0)

        for char, child in current_node.children.items():
            queue.append(child)
            link_node = current_node.link

            while link_node is not None and char not in link_node.children:
                link_node = link_node.link

            child.link = link_node.children[char] if link_node else root
            child.words_in_node += child.link.words_in_node


def aho_corasick(text, keywords):
    root = build_trie(keywords)
    build_link_transitions(root)

    current_node = root
    matches = []

    for i, char in enumerate(text):
        while current_node is not None and char not in current_node.children:
            current_node = current_node.link

        if current_node is None:
            current_node = root
            continue

        current_node = current_node.children[char]

        for keyword in current_node.words_in_node:
            matches.append((i - len(keyword) + 1, keyword))

    return matches



text = "applebanana"
keywords = ["app", "banana", "ana"]

matches = aho_corasick(text, keywords)
for match in matches:
    print(f"Position: {match[0]} word: {match[1]}")