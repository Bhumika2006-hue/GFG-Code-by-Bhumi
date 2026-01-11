class Solution:
    def luckyPermutations(self, N, M, arr, graph):
        # 1. Build Adjacency Matrix
        # Note: Nodes in graph are 1-based, convert to 0-based if necessary
        adj = [[False] * (N + 1) for _ in range(N + 1)]
        for u, v in graph:
            adj[u][v] = adj[v][u] = True
            
        # 2. DP table: dp[mask][last_index]
        # mask: bitmask of indices from arr used
        # last_index: the index of the element in arr that was added last
        dp = [[0] * N for _ in range(1 << N)]
        
        # 3. Base Case: Paths of length 1
        for i in range(N):
            dp[1 << i][i] = 1
            
        # 4. Fill DP Table
        for mask in range(1, 1 << N):
            for last in range(N):
                if dp[mask][last] == 0:
                    continue
                
                # Try adding the next element
                for next_idx in range(N):
                    # If next_idx is not in the mask
                    if not (mask & (1 << next_idx)):
                        # Check if there's an edge between arr[last] and arr[next_idx]
                        if adj[arr[last]][arr[next_idx]]:
                            dp[mask | (1 << next_idx)][next_idx] += dp[mask][last]
                            
        # 5. Sum all paths that include all nodes (mask = all 1s)
        ans = 0
        full_mask = (1 << N) - 1
        for i in range(N):
            ans += dp[full_mask][i]
            
        return ans