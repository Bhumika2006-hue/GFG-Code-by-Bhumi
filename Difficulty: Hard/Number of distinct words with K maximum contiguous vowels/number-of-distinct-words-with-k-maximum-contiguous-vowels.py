class Solution:
    def kvowelwords(self, N, K):
        MOD = 1000000007
        
        # dp[i][j] = number of words of length i ending with j vowels
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        
        # Base case: Word of length 0
        dp[0][0] = 1
        
        for i in range(1, N + 1):
            # Calculate the sum of all valid words of length i-1 
            # to handle the consonant case (resetting the vowel count)
            sum_prev = sum(dp[i-1]) % MOD
            
            for j in range(K + 1):
                if j == 0:
                    # Current char is a consonant (21 options)
                    # Can follow any word of length i-1
                    dp[i][j] = (sum_prev * 21) % MOD
                else:
                    # Current char is a vowel (5 options)
                    # Must follow a word ending in j-1 vowels
                    dp[i][j] = (dp[i-1][j-1] * 5) % MOD
                    
        # The answer is the sum of all words of length N 
        # ending in 0, 1, ..., K vowels
        return sum(dp[N]) % MOD