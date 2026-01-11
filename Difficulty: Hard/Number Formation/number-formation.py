class Solution:
    def getSum(self, X, Y, Z):
        MOD = 10**9 + 7
        
        # Initialize 3D arrays for sum and count
        # sum_dp[i][j][k] stores sum of numbers with i 4s, j 5s, k 6s
        # count_dp[i][j][k] stores how many such numbers exist
        sum_dp = [[[0] * (Z + 1) for _ in range(Y + 1)] for _ in range(X + 1)]
        count_dp = [[[0] * (Z + 1) for _ in range(Y + 1)] for _ in range(X + 1)]
        
        # Base case: 0 numbers formed with 0 digits is 1 (the empty string/number)
        count_dp[0][0][0] = 1
        total_sum = 0
        
        for i in range(X + 1):
            for j in range(Y + 1):
                for k in range(Z + 1):
                    # Form numbers by adding 4
                    if i > 0:
                        count_dp[i][j][k] = (count_dp[i][j][k] + count_dp[i-1][j][k]) % MOD
                        sum_dp[i][j][k] = (sum_dp[i][j][k] + sum_dp[i-1][j][k] * 10 + 4 * count_dp[i-1][j][k]) % MOD
                    
                    # Form numbers by adding 5
                    if j > 0:
                        count_dp[i][j][k] = (count_dp[i][j][k] + count_dp[i][j-1][k]) % MOD
                        sum_dp[i][j][k] = (sum_dp[i][j][k] + sum_dp[i][j-1][k] * 10 + 5 * count_dp[i][j-1][k]) % MOD
                        
                    # Form numbers by adding 6
                    if k > 0:
                        count_dp[i][j][k] = (count_dp[i][j][k] + count_dp[i][j][k-1]) % MOD
                        sum_dp[i][j][k] = (sum_dp[i][j][k] + sum_dp[i][j][k-1] * 10 + 6 * count_dp[i][j][k-1]) % MOD
                    
                    # Add current combination's sum to the final answer
                    total_sum = (total_sum + sum_dp[i][j][k]) % MOD
                    
        return total_sum