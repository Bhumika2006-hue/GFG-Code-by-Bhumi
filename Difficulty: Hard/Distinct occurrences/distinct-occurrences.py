class Solution:
    def subseqCount(self, txt, pat):
        n = len(txt)
        m = len(pat)
        
        # If pattern is longer than text, it can't be a subsequence
        if m > n:
            return 0
            
        # dp[i] will store the count of occurrences of pat[0...i-1]
        # Base case: empty pattern has 1 occurrence in any text
        dp = [0] * (m + 1)
        dp[0] = 1
        
        # Iterate through each character of the text
        for j in range(1, n + 1):
            # Iterate backwards through the pattern to use values 
            # from the previous text character iteration
            for i in range(m, 0, -1):
                if txt[j-1] == pat[i-1]:
                    dp[i] = dp[i] + dp[i-1]
                # If they don't match, dp[i] remains the same (dp[i][j-1])
                    
        return dp[m]