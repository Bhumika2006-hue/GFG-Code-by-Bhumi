class Solution:

    def optimalKeys(self, n: int) -> int:
        # If n is small (less than 7), the max 'A's is just n (pressing 'A' n times)
        if n <= 6:
            return n
        
        # dp[i] stores the maximum number of 'A's with i keystrokes
        dp = [0] * (n + 1)
        
        # Initializing base cases for 1 to 6
        for i in range(1, 7):
            dp[i] = i
            
        for i in range(7, n + 1):
            # Option 1: Just press 'A' (though for i > 6, this is rarely optimal)
            dp[i] = dp[i - 1] + 1
            
            # Option 2: Try different "break points" to start the Select + Copy + Paste sequence
            # We look back starting from 3 steps ago (Select, Copy, Paste)
            for j in range(i - 3, 0, -1):
                # dp[j] is the count before Ctrl-A + Ctrl-C
                # (i - j - 1) represents the multiplier effect of pasting
                current_value = dp[j] * (i - j - 1)
                if current_value > dp[i]:
                    dp[i] = current_value
                    
        return dp[n]
