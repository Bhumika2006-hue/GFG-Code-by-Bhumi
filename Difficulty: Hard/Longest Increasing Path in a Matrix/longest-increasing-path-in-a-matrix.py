import sys

# Increase recursion depth for large matrices
sys.setrecursionlimit(10**6)

class Solution:
    def longIncPath(self, matrix, n, m):
        if not matrix or not matrix[0]:
            return 0
        
        # memo[i][j] will store the longest path starting from cell (i, j)
        memo = [[0] * m for _ in range(n)]
        
        def dfs(r, c):
            # If already calculated, return the stored value
            if memo[r][c] != 0:
                return memo[r][c]
            
            max_p = 1
            # Directions: Right, Left, Down, Up
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and the strictly increasing condition
                if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] > matrix[r][c]:
                    max_p = max(max_p, 1 + dfs(nr, nc))
            
            # Store result in memo table
            memo[r][c] = max_p
            return max_p

        ans = 0
        # Iterate through every cell to find the global maximum
        for r in range(n):
            for c in range(m):
                if memo[r][c] == 0:
                    ans = max(ans, dfs(r, c))
                else:
                    ans = max(ans, memo[r][c])
                
        return ans