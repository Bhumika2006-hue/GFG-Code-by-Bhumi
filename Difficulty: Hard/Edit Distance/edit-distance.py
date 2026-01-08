class Solution:
    def editDistance(self, s1, s2):
        m, n = len(s1), len(s2)
        
        # We use two rows to optimize space from O(m*n) to O(n)
        # prev represents dp[i-1], curr represents dp[i]
        prev = list(range(n + 1))
        curr = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr[0] = i # Base case: converting s1[0...i] to empty s2
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    # Characters match, no operation needed
                    curr[j] = prev[j-1]
                else:
                    # Minimum of (Insert, Remove, Replace) + 1
                    curr[j] = 1 + min(curr[j-1],  # Insert
                                      prev[j],    # Remove
                                      prev[j-1])  # Replace
            # Move current row to previous for next iteration
            prev = curr[:]
            
        return prev[n]