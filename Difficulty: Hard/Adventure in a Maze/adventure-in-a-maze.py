class Solution:
    def FindWays(self, matrix):
        n = len(matrix)
        MOD = 10**9 + 7
        
        # ways[i][j] stores total paths to (i, j)
        ways = [[0] * n for _ in range(n)]
        # adv[i][j] stores max adventure sum to (i, j)
        adv = [[0] * n for _ in range(n)]
        
        # Initial position
        ways[0][0] = 1
        adv[0][0] = matrix[0][0]
        
        for i in range(n):
            for j in range(n):
                # If current cell is unreachable, skip it
                if ways[i][j] == 0:
                    continue
                
                cell_val = matrix[i][j]
                
                # Check Right move (1 or 3)
                if cell_val == 1 or cell_val == 3:
                    if j + 1 < n:
                        # Update ways
                        ways[i][j+1] = (ways[i][j+1] + ways[i][j]) % MOD
                        # Update max adventure
                        adv[i][j+1] = max(adv[i][j+1], adv[i][j] + matrix[i][j+1])
                
                # Check Down move (2 or 3)
                if cell_val == 2 or cell_val == 3:
                    if i + 1 < n:
                        # Update ways
                        ways[i+1][j] = (ways[i+1][j] + ways[i][j]) % MOD
                        # Update max adventure
                        adv[i+1][j] = max(adv[i+1][j], adv[i][j] + matrix[i+1][j])
        
        # Final answer at Bottom Right corner
        total_ways = ways[n-1][n-1]
        max_adventure = adv[n-1][n-1] if total_ways > 0 else 0
        
        return [total_ways, max_adventure]