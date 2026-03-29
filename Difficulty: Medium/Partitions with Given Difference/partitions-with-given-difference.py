class Solution:
    def countPartitions(self, arr, diff):
        total = sum(arr)
        
        # Invalid cases
        if (total + diff) % 2 != 0 or total < diff:
            return 0
        
        target = (total + diff) // 2
        
        dp = [0] * (target + 1)
        dp[0] = 1  # base case
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target]