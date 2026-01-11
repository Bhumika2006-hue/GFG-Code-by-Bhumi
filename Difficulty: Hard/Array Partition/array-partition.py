class Solution:
    def partitionArray(self, N, K, M, A):
        # 1. Sort the array to ensure contiguous partitions are optimal
        A.sort()
        
        # dp[i] will be True if the first i elements can be partitioned
        dp = [False] * (N + 1)
        dp[0] = True
        
        # valid_indices stores indices j where dp[j] is True 
        # and they are within the potential range for the current i
        from collections import deque
        valid_indices = deque()
        
        # j is the start index of the current potential partition
        j = 0
        
        for i in range(1, N + 1):
            # Maintain the window of possible j such that j <= i - K
            # We check if dp[j] is true for indices that could start a partition ending at i
            if i >= K:
                if dp[i - K]:
                    valid_indices.append(i - K)
            
            # Remove indices from the left that violate the Max - Min <= M rule
            # Since A is sorted, A[i-1] is max and A[valid_indices[0]] is min
            while valid_indices and A[i - 1] - A[valid_indices[0]] > M:
                valid_indices.popleft()
            
            # If there's any j in the queue, it means there is a valid dp[j] 
            # that satisfies both the size >= K and diff <= M constraints
            if valid_indices:
                dp[i] = True
        
        return dp[N]