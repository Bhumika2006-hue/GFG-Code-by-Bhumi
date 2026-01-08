class Solution:
    def distinctSubseq(self, s):
        n = len(s)
        MOD = 10**9 + 7
        
        # dp[i] stores the number of distinct subsequences of s[0...i-1]
        dp = [0] * (n + 1)
        
        # Base case: an empty string has 1 subsequence ("")
        dp[0] = 1
        
        # Map to store the last position (1-based index) of each character
        last_seen = {}
        
        for i in range(1, n + 1):
            char = s[i-1]
            
            # Initially, the number of subsequences doubles
            dp[i] = (2 * dp[i-1]) % MOD
            
            # If the character appeared before, subtract the subsequences 
            # that were available before its last occurrence.
            if char in last_seen:
                prev_idx = last_seen[char]
                dp[i] = (dp[i] - dp[prev_idx - 1] + MOD) % MOD
            
            # Record the latest position of this character
            last_seen[char] = i
            
        return dp[n]