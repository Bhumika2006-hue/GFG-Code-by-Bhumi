class Solution:
    def minDifference(self, arr):
        n = len(arr)
        total_sum = sum(arr)
        
        # We only need to check sums up to total_sum // 2
        target = total_sum // 2
        
        # dp[i] will be True if a subset with sum i exists
        dp = [False] * (target + 1)
        dp[0] = True
        
        # Standard 0/1 Knapsack style DP optimization (Space Optimized)
        for num in arr:
            # Iterate backwards to ensure each element is used only once
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
                    
        # Find the largest j such that dp[j] is True
        for j in range(target, -1, -1):
            if dp[j]:
                # If s1 = j, then s2 = total_sum - j
                # Difference = (total_sum - j) - j = total_sum - 2*j
                return total_sum - 2 * j
                
        return total_sum