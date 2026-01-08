class Solution:
    def knapsack(self, W, val, wt):
        n = len(wt)
        
        # dp[i] will store the maximum value for knapsack capacity i
        # Initialize with 0
        dp = [0] * (W + 1)
        
        # Iterate through all items
        for i in range(n):
            current_weight = wt[i]
            current_value = val[i]
            
            # Iterate backwards through the dp array
            # We go backwards to ensure each item is used only once
            # (If we went forwards, it would become the Unbounded Knapsack problem)
            for j in range(W, current_weight - 1, -1):
                # Max of (not picking the item) and (picking the item)
                dp[j] = max(dp[j], current_value + dp[j - current_weight])
                
        return dp[W]
