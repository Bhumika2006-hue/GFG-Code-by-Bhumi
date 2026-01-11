class Solution:
    def maxSkill(self, arr):
        # Step 1: Add boundary 1s to handle out-of-bounds cases
        nums = [1] + arr + [1]
        n = len(nums)
        
        # Step 2: Initialize DP table
        # dp[i][j] will store the max skill for the range strictly between i and j
        dp = [[0] * n for _ in range(n)]
        
        # Step 3: Iterate through all possible range lengths
        # 'length' is the distance between i and j
        for length in range(2, n):
            # Iterate through all possible starting points i
            for i in range(n - length):
                j = i + length
                
                # Try every person k between i and j as the LAST one to be removed
                for k in range(i + 1, j):
                    # Skill = skill from left sub-range + current removal + skill from right sub-range
                    current_skill = dp[i][k] + (nums[i] * nums[k] * nums[j]) + dp[k][j]
                    
                    if current_skill > dp[i][j]:
                        dp[i][j] = current_skill
                        
        return dp[0][n-1]