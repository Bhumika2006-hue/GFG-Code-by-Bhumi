import math

class Solution:
    def solveQueries(self, nums, Queries, k):
        n = len(nums)
        q = len(Queries)
        block_size = int(math.sqrt(n)) + 1
        
        # Adjust queries to 0-indexed and store original index for output order
        formatted_queries = []
        for i in range(q):
            l, r = Queries[i]
            formatted_queries.append((l - 1, r - 1, i))
            
        # Sort queries based on block index and R position
        formatted_queries.sort(key=lambda x: (x[0] // block_size, x[1]))
        
        # State variables
        freq = [0] * 1001  # nums[i] <= 1000 based on constraints
        at_least_k = 0
        results = [0] * q
        
        curr_L, curr_R = 0, -1
        
        def add(val):
            nonlocal at_least_k
            freq[val] += 1
            if freq[val] == k:
                at_least_k += 1
                
        def remove(val):
            nonlocal at_least_k
            if freq[val] == k:
                at_least_k -= 1
            freq[val] -= 1

        # Process queries
        for l, r, idx in formatted_queries:
            # Move R pointer forward
            while curr_R < r:
                curr_R += 1
                add(nums[curr_R])
            # Move R pointer backward
            while curr_R > r:
                remove(nums[curr_R])
                curr_R -= 1
            # Move L pointer forward
            while curr_L < l:
                remove(nums[curr_L])
                curr_L += 1
            # Move L pointer backward
            while curr_L > l:
                curr_L -= 1
                add(nums[curr_L])
            
            results[idx] = at_least_k
            
        return results