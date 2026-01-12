class TrieNode:
    def __init__(self):
        self.links = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        # Process from MSB (30th bit) to LSB (0th bit)
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            if not node.links[bit]:
                node.links[bit] = TrieNode()
            node = node.links[bit]

    def get_max_xor(self, num):
        node = self.root
        max_xor = 0
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            # To maximize XOR, we want the opposite bit
            desired_bit = 1 - bit
            if node.links[desired_bit]:
                max_xor |= (1 << i)
                node = node.links[desired_bit]
            else:
                node = node.links[bit]
        return max_xor

class Solution:
    def maxXor(self, arr, queries):
        n = len(arr)
        q = len(queries)
        
        # Sort arr to process elements incrementally
        arr.sort()
        
        # Keep track of original query indices to return answer in correct order
        # query format: (m_i, x_i, original_index)
        offline_queries = []
        for i in range(q):
            offline_queries.append((queries[i][1], queries[i][0], i))
        
        # Sort queries based on m_i
        offline_queries.sort()
        
        trie = Trie()
        ans = [-1] * q
        arr_idx = 0
        
        for m_val, x_val, q_idx in offline_queries:
            # Add all elements from arr that are <= current m_val into the Trie
            while arr_idx < n and arr[arr_idx] <= m_val:
                trie.insert(arr[arr_idx])
                arr_idx += 1
            
            # If no elements were added, Trie only has the empty root
            if arr_idx > 0:
                ans[q_idx] = trie.get_max_xor(x_val)
            else:
                ans[q_idx] = -1
                
        return ans