class Solution:
    def minCutCost(self, n, cuts):
        # 1. Add boundaries and sort the cuts
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)
        
        # 2. Initialize DP table
        # dp[i][j] is the min cost to cut a stick from cuts[i] to cuts[j]
        dp = [[0] * m for _ in range(m)]
        
        # 3. Fill the DP table based on the length of the interval
        # length is the number of cut points in the segment (minimum 2)
        for length in range(2, m):
            for i in range(m - length):
                j = i + length
                
                # If length is 2, there are no points between i and j to cut
                if length == 2:
                    dp[i][j] = cuts[j] - cuts[i]
                else:
                    res = float('inf')
                    # Try every possible intermediate cut point k
                    for k in range(i + 1, j):
                        res = min(res, dp[i][k] + dp[k][j])
                    
                    # Add the cost of the current cut (current stick length)
                    dp[i][j] = (cuts[j] - cuts[i]) + res
        
        # The answer is the cost for the full stick from cuts[0] to cuts[m-1]
        # Adjusting logic: if only 1 cut, the above logic works.
        # However, a cleaner base case is: 
        # intervals of length 1 (adjacent cuts) cost 0 to "finish"
        
        # Re-fined loop for clarity:
        dp = [[0] * m for _ in range(m)]
        for diff in range(2, m): # diff is j - i
            for i in range(m - diff):
                j = i + diff
                res = float('inf')
                for k in range(i + 1, j):
                    res = min(res, dp[i][k] + dp[k][j])
                dp[i][j] = (cuts[j] - cuts[i]) + res
                
        return dp[0][m - 1]