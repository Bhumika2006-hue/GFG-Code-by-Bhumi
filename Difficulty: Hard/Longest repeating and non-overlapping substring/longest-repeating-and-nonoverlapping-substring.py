class Solution:
    def longestSubstring(self, s):
        n = len(s)
        # dp[i][j] stores the length of the longest non-overlapping 
        # repeating substring ending at index i-1 and j-1
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        max_len = 0
        end_index = 0
        
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                # If characters match and don't overlap
                # The gap (j - i) must be >= the current matching length
                if s[i-1] == s[j-1] and dp[i-1][j-1] < (j - i):
                    dp[i][j] = dp[i-1][j-1] + 1
                    
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_index = i
                else:
                    dp[i][j] = 0
        
        # If no repeating non-overlapping substring is found, return "-1"
        if max_len > 0:
            return s[end_index - max_len : end_index]
        else:
            return "-1"