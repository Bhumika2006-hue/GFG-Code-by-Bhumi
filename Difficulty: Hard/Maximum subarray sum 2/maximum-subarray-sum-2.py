from collections import deque

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        # Compute Prefix Sums (size n+1 to handle sums starting from index 0)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
            
        max_sum = -float('inf')
        dq = deque()
        
        # We iterate through possible end positions 'i' of the subarray
        # The valid range for the starting prefix sum index 'k' is [i-b, i-a]
        for i in range(a, n + 1):
            # 1. Add the new candidate for the start of the subarray: P[i-a]
            new_val_idx = i - a
            
            # Maintain the deque in increasing order of prefix_sum values
            while dq and prefix_sum[dq[-1]] >= prefix_sum[new_val_idx]:
                dq.pop()
            dq.append(new_val_idx)
            
            # 2. Remove indices that are now outside the length constraint: k < i-b
            if dq[0] < i - b:
                dq.popleft()
            
            # 3. Calculate max subarray sum ending at i
            # The smallest prefix_sum in the valid window is at the front
            current_max = prefix_sum[i] - prefix_sum[dq[0]]
            max_sum = max(max_sum, current_max)
            
        return max_sum