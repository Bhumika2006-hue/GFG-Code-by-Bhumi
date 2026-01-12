class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Solution:
    def countSubarrays(self, arr, k):
        root = TrieNode()
        
        def insert(val):
            node = root
            for i in range(14, -1, -1):
                bit = (val >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
                node.count += 1
        
        def query(val, k):
            node = root
            count = 0
            for i in range(14, -1, -1):
                if not node: break
                bit_v = (val >> i) & 1
                bit_k = (k >> i) & 1
                
                if bit_k == 1:
                    # If bit in k is 1, all elements in the subtree 
                    # where XOR bit is 0 are strictly less than k.
                    if node.children[bit_v]:
                        count += node.children[bit_v].count
                    # Move to the subtree where XOR bit is 1 to check further bits
                    node = node.children[1 - bit_v]
                else:
                    # If bit in k is 0, we must go to the subtree where XOR bit is 0
                    node = node.children[bit_v]
            
            if node:
                count += node.count
            return count

        ans = 0
        curr_xor = 0
        insert(0) # Handle subarrays starting from index 0
        for num in arr:
            curr_xor ^= num
            ans += query(curr_xor, k)
            insert(curr_xor)
        return ans

    def minimizeKForXOR(self, x, arr):
        low = 0
        high = 2**14 # Max value based on constraints (10^4)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if self.countSubarrays(arr, mid) >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans