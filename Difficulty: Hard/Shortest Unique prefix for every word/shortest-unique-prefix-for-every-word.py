class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes
        self.children = {}
        # Count how many words share this prefix
        self.count = 0

class Solution:
    def findPrefixes(self, arr, N):
        root = TrieNode()
        
        # Step 1: Insert all words into the Trie
        for word in arr:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                # Increment the count of words passing through this node
                curr.count += 1
        
        result = []
        
        # Step 2: For each word, find the shortest unique prefix
        for word in arr:
            prefix = ""
            curr = root
            for char in word:
                prefix += char
                curr = curr.children[char]
                # If count is 1, this prefix is unique
                if curr.count == 1:
                    break
            result.append(prefix)
            
        return result