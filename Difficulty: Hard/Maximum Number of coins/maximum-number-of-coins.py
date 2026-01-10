class Solution():
    def maxCoins(self, N, a):
        # Step 1: Add boundary 1s as per problem statement
        nums = [1] + a + [1]
        n = len(nums)
        
        # Step 2: Initialize DP table
        # dp[i][j] represents max coins from bursting balloons between i and j
        dp = [[0] * n for _ in range(n)]
        
        # Step 3: Iterate through all possible interval lengths
        # length is the distance between i and j
        for length in range(2, n):
            # Iterate through all possible starting points i
            for i in range(n - length):
                j = i + length
                
                # Pick every k between i and j to be the LAST balloon burst
                for k in range(i + 1, j):
                    # coins = left_interval + burst_k_last + right_interval
                    coins = dp[i][k] + (nums[i] * nums[k] * nums[j]) + dp[k][j]
                    dp[i][j] = max(dp[i][j], coins)
                    
        return dp[0][n-1]