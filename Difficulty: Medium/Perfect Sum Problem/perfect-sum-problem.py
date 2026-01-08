class Solution:
    def perfectSum(self, arr, target):
        # n is the size of the array
        # target is the sum we are looking for
        
        # Initialize DP array with 0s, dp[i] will store count of subsets with sum i
        dp = [0] * (target + 1)
        
        # Base case: There is one way to get sum 0 (the empty subset)
        dp[0] = 1
        
        # Process each number in the array
        for num in arr:
            # Iterate backwards to ensure each element is used only once per subset
            # We go down to 'num' because any index smaller than 'num' 
            # cannot be part of a subset that includes 'num'
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]
        
        return dp[target]