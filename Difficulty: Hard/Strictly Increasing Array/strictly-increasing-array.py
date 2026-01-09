class Solution:
    def min_operations(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
            
        # Step 1: Transform the array
        # B[i] = nums[i] - i
        # Now we just need to find the Longest Non-Decreasing Subsequence of B
        B = []
        for i in range(n):
            B.append(nums[i] - i)
            
        # Step 2: Find Longest Non-Decreasing Subsequence length in O(n log n)
        # We use a tails array and binary search (bisect_right for non-decreasing)
        import bisect
        
        tails = []
        for x in B:
            # Use bisect_right to allow duplicate values (Non-Decreasing)
            idx = bisect.bisect_right(tails, x)
            if idx < len(tails):
                tails[idx] = x
            else:
                tails.append(x)
                
        # Length of LNDS is the size of tails
        max_keep = len(tails)
        
        # Min operations = Total elements - elements we kept
        return n - max_keep