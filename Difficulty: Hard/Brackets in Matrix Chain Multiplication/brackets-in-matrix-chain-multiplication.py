class Solution:
    def matrixChainOrder(self, arr):
        n = len(arr) - 1  # Number of matrices
        # dp[i][j] will store the minimum multiplication cost of Ai...Aj
        dp = [[0] * n for _ in range(n)]
        # bracket[i][j] will store the optimal split point k
        bracket = [[0] * n for _ in range(n)]
        
        # l is the chain length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    # Cost = cost of left + cost of right + cost of multiplying results
                    cost = dp[i][k] + dp[k+1][j] + (arr[i] * arr[k+1] * arr[j+1])
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        bracket[i][j] = k
        
        # Helper function to reconstruct the string from the split points
        def get_string(i, j):
            if i == j:
                # Convert index 0 -> 'A', 1 -> 'B', etc.
                return chr(ord('A') + i)
            
            k = bracket[i][j]
            left_part = get_string(i, k)
            right_part = get_string(k + 1, j)
            
            return "(" + left_part + right_part + ")"
            
        return get_string(0, n - 1)