class Solution:
    def countSubsequences(self, s):
        n = len(s)
        # dp[i] will store the count of distinct subsequences of s[0...i-1]
        dp = [0] * (n + 1)
        
        # Base case: empty string has 1 subsequence ("")
        dp[0] = 1
        
        # Dictionary to keep track of the last seen index of each character
        last_seen = {}
        
        for i in range(1, n + 1):
            char = s[i-1]
            
            # Double the count from the previous step
            dp[i] = 2 * dp[i-1]
            
            # If the character has appeared before, subtract duplicates
            if char in last_seen:
                prev_idx = last_seen[char]
                dp[i] = dp[i] - dp[prev_idx - 1]
            
            # Mark the current position as the last seen for this character
            last_seen[char] = i
            
        return dp[n]

    def betterString(self, s1, s2):
        # Calculate distinct subsequences for both s1 and s2
        res1 = self.countSubsequences(s1)
        res2 = self.countSubsequences(s2)
        
        # Return s2 if it has more distinct subsequences, otherwise return s1
        if res2 > res1:
            return s2
        return s1