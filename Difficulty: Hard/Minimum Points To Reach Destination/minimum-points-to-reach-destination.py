class Solution:
    def minPoints(self, m, n, points):
        # dp[i][j] represents the min points needed at cell (i, j)
        dp = [[0] * n for _ in range(m)]

        # Base Case: The destination cell
        # We need at least 1 point after adding the value at the destination
        dp[m-1][n-1] = max(1, 1 - points[m-1][n-1])

        # Fill the last row (can only move right)
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - points[m-1][j])

        # Fill the last column (can only move down)
        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - points[i][n-1])

        # Fill the rest of the DP table
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                # You pick the path (down or right) that requires FEWER points
                min_exit_points = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, min_exit_points - points[i][j])

        return dp[0][0]