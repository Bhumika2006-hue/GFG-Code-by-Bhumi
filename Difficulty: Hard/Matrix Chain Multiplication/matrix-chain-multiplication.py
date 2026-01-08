class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        # If there's only one matrix, no multiplication is needed
        if n <= 2:
            return 0
            
        # num_matrices = n - 1
        # dp[i][j] will store the minimum multiplication cost of Mi...Mj
        # We use (n) size to maintain 1-based indexing for matrices easily
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # l is the chain length. We start from length 2 up to the total number of matrices.
        for l in range(2, n): 
            for i in range(1, n - l + 1):
                j = i + l - 1
                dp[i][j] = float('inf')
                
                # Try every possible split point k
                for k in range(i, j):
                    # cost = cost of left subchain + cost of right subchain + cost of joining
                    cost = dp[i][k] + dp[k+1][j] + (arr[i-1] * arr[k] * arr[j])
                    
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        
        return dp[1][n-1]