class Solution:
    def countWays(self, s):
        # Separate symbols and operators
        symbols = []
        operators = []
        for i in range(len(s)):
            if i % 2 == 0:
                symbols.append(s[i])
            else:
                operators.append(s[i])
        
        n = len(symbols)
        # dp[i][j][0] = False ways, dp[i][j][1] = True ways
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        
        # Base Case: Single symbols
        for i in range(n):
            if symbols[i] == 'T':
                dp[i][i][1] = 1
            else:
                dp[i][i][0] = 1
        
        # Gap-based DP (Interval length from 2 to n)
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i, j):
                    # Results from left and right sub-expressions
                    lt, lf = dp[i][k][1], dp[i][k][0]
                    rt, rf = dp[k+1][j][1], dp[k+1][j][0]
                    
                    op = operators[k]
                    
                    if op == '&':
                        dp[i][j][1] += (lt * rt)
                        dp[i][j][0] += (lt * rf + lf * rt + lf * rf)
                    elif op == '|':
                        dp[i][j][1] += (lt * rt + lt * rf + lf * rt)
                        dp[i][j][0] += (lf * rf)
                    elif op == '^':
                        dp[i][j][1] += (lt * rf + lf * rt)
                        dp[i][j][0] += (lt * rt + lf * rf)
        
        return dp[0][n-1][1]