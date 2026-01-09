class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node.current_node = node.children[char]
            node = node.children[char]
        node.is_end = True

    def get_words_from_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return ["0"]
            node = node.children[char]
        
        # DFS to find all words starting from this node
        result = []
        self._dfs(node, prefix, result)
        return sorted(result)

    def _dfs(self, node, current_prefix, result):
        if node.is_end:
            result.append(current_prefix)
        
        # Explore children in alphabetical order
        for char in sorted(node.children.keys()):
            self._dfs(node.children[char], current_prefix + char, result)

class Solution:
    def displayContacts(self, n, contact, s):
        # Remove duplicates and initialize Trie
        unique_contacts = set(contact)
        trie = Trie()
        for c in unique_contacts:
            trie.insert(c)
        
        ans = []
        prefix = ""
        found_failure = False
        
        for char in s:
            prefix += char
            if found_failure:
                ans.append(["0"])
                continue
            
            matches = trie.get_words_from_prefix(prefix)
            if matches == ["0"]:
                found_failure = True
            ans.append(matches)
            
        return ans