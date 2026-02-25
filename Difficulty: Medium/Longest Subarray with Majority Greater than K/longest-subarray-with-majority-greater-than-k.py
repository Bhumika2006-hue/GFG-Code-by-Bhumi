class Solution:
    def longestSubarray(self, arr, k):
        prefix = 0
        first = {}
        ans = 0
        
        for i, x in enumerate(arr):
            if x > k:
                prefix += 1
            else:
                prefix -= 1
            
            # Case 1: whole subarray [0..i] is valid
            if prefix > 0:
                ans = i + 1
            else:
                # Case 2: find smaller prefix
                if prefix - 1 in first:
                    ans = max(ans, i - first[prefix - 1])
            
            # store first occurrence
            if prefix not in first:
                first[prefix] = i
        
        return ans
