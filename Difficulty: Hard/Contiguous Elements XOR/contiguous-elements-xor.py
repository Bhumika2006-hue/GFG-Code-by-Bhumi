class TrieNode:
    def __init__(self):
        # Each node has two children: 0 and 1
        self.children = {}

class Solution:
    def insert(self, root, num):
        curr = root
        # Process 20 bits (since 10^6 < 2^20)
        for i in range(19, -1, -1):
            bit = (num >> i) & 1
            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]

    def query(self, root, num):
        curr = root
        max_xor = 0
        for i in range(19, -1, -1):
            bit = (num >> i) & 1
            # To maximize XOR, we want the opposite bit
            desired = 1 - bit
            if desired in curr.children:
                max_xor |= (1 << i)
                curr = curr.children[desired]
            else:
                curr = curr.children[bit]
        return max_xor

    def maxSubarrayXOR(self, arr, n):
        root = TrieNode()
        # Insert 0 to handle cases where the subarray starts from index 0
        self.insert(root, 0)
        
        prefix_xor = 0
        result = 0
        
        for val in arr:
            prefix_xor ^= val
            # Insert current prefix into Trie
            self.insert(root, prefix_xor)
            # Find the max XOR possible with any previous prefix
            result = max(result, self.query(root, prefix_xor))
            
        return result