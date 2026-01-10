import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(10**5)

class Solution:
    def articulationPoints(self, V, adj_list):
        # disc[i]: discovery time of node i
        # low[i]: lowest discovery time reachable from node i using back-edges
        disc = [-1] * V
        low = [-1] * V
        is_ap = [False] * V # Track APs to avoid duplicates
        self.timer = 0
        
        # Convert edges to adjacency list if input is edges[][]
        # For GFG, adj is usually passed directly as a list of lists
        adj = [[] for _ in range(V)]
        for u, v in adj_list:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u, p=-1):
            disc[u] = low[u] = self.timer
            self.timer += 1
            children = 0
            
            for v in adj[u]:
                if v == p:
                    continue
                
                if disc[v] == -1:  # Node v is not visited
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    
                    # Case 1: Non-root node condition
                    if p != -1 and low[v] >= disc[u]:
                        is_ap[u] = True
                else:
                    # Update low value for back-edge
                    low[u] = min(low[u], disc[v])
            
            # Case 2: Root node condition
            if p == -1 and children > 1:
                is_ap[u] = True

        # Handle disconnected components
        for i in range(V):
            if disc[i] == -1:
                dfs(i)

        ans = [i for i, val in enumerate(is_ap) if val]
        return ans if ans else [-1]