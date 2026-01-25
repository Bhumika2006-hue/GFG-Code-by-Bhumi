class Solution:
    def findWays(self, n):
        if n % 2 == 1:
            return 0
        
        m = n // 2
        dp = [0] * (m + 1)
        dp[0] = 1
        
        for i in range(1, m + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        
        return dp[m]
