import sys

# Increase recursion depth for large matrices
sys.setrecursionlimit(10**6)

class Solution:
    def closedIslands(self, matrix, N, M):
        
        def dfs(r, c):
            # Base case: out of bounds or water
            if r < 0 or r >= N or c < 0 or c >= M or matrix[r][c] == 0:
                return
            
            # Sink the land to avoid re-visiting
            matrix[r][c] = 0
            
            # Explore 4-directional neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Remove islands connected to boundaries
        # Check first and last rows
        for j in range(M):
            if matrix[0][j] == 1:
                dfs(0, j)
            if matrix[N-1][j] == 1:
                dfs(N-1, j)
                
        # Check first and last columns
        for i in range(N):
            if matrix[i][0] == 1:
                dfs(i, 0)
            if matrix[i][M-1] == 1:
                dfs(i, M-1)

        # Step 2: Count the remaining isolated islands
        count = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    count += 1
                    dfs(i, j)
                    
        return count