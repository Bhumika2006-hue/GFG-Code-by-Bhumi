from bisect import bisect_left

class Solution:
    def minDifference(self, N, A):
        # Step 1: Compute Prefix Sums
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + A[i]
            
        def get_best_split(start, end):
            """
            Finds a cut in prefix[start:end+1] such that the two resulting 
            subarray sums are as close as possible.
            """
            total_sum = prefix[end] - prefix[start]
            target = prefix[start] + total_sum / 2
            
            # Binary search for the index where prefix sum is closest to target
            idx = bisect_left(prefix, target, start + 1, end)
            
            # We check the index found and the one before it to find the absolute best
            best_diff = float('inf')
            best_sums = (0, 0)
            
            for k in [idx - 1, idx]:
                if start < k < end:
                    sum1 = prefix[k] - prefix[start]
                    sum2 = prefix[end] - prefix[k]
                    if abs(sum1 - sum2) < best_diff:
                        best_diff = abs(sum1 - sum2)
                        best_sums = (sum1, sum2)
            return best_sums

        ans = float('inf')
        
        # Step 2: Iterate over the middle cut (separating Q and R)
        # P, Q must have at least 1 element each (2 elements total)
        # R, S must have at least 1 element each (2 elements total)
        for i in range(2, N - 1):
            # Left side split (P and Q)
            W, X = get_best_split(0, i)
            # Right side split (R and S)
            Y, Z = get_best_split(i, N)
            
            current_max = max(W, X, Y, Z)
            current_min = min(W, X, Y, Z)
            ans = min(ans, current_max - current_min)
            
        return ans