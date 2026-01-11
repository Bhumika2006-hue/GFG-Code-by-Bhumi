class Solution:
    def minCost(self, keys, freq):
        n = len(keys)
        # dp[i][j] will store the min cost for keys from index i to j
        dp = [[0] * n for _ in range(n)]
        
        # prefix_sum[i] stores sum of freq[0...i-1]
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + freq[i]
            
        def get_sum(i, j):
            return prefix_sum[j+1] - prefix_sum[i]

        # length is the number of keys in the current range
        for length in range(1, n + 1):
            # i is the starting index
            for i in range(n - length + 1):
                j = i + length - 1
                
                if length == 1:
                    dp[i][j] = freq[i]
                    continue
                
                res = float('inf')
                
                # Try every key in the range [i, j] as the root
                for r in range(i, j + 1):
                    # Cost = left subtree + right subtree
                    left = dp[i][r-1] if r > i else 0
                    right = dp[r+1][j] if r < j else 0
                    
                    res = min(res, left + right)
                
                # Add the sum of all frequencies in the current range
                dp[i][j] = res + get_sum(i, j)
                
        return dp[0][n-1]