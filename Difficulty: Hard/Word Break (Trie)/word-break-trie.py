class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def wordBreak(self, A, B):
        # 1. Build the Trie
        root = TrieNode()
        for word in B:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isEndOfWord = True
            
        n = len(A)
        # 2. Memoization table to store results of subproblems
        memo = {}

        def canBreak(start):
            # Base case: reached the end of the string
            if start == n:
                return True
            
            # If we've calculated this starting position before, return it
            if start in memo:
                return memo[start]
            
            curr = root
            # Traverse string A starting from 'start'
            for i in range(start, n):
                char = A[i]
                
                # If the character path doesn't exist in Trie, 
                # no more words can start from 'start' using this path
                if char not in curr.children:
                    break
                
                curr = curr.children[char]
                
                # If we found a valid word in the dictionary
                if curr.isEndOfWord:
                    # Recursively check if the remaining string can be broken
                    if canBreak(i + 1):
                        memo[start] = True
                        return True
            
            # If no valid segmentation was found
            memo[start] = False
            return False

        # Return 1 for True, 0 for False
        return 1 if canBreak(0) else 0