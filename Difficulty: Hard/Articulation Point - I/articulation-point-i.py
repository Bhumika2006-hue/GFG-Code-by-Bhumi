import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(10**6)

class Solution:
    def articulationPoints(self, V, adj):
        disc = [-1] * V      # Discovery time of nodes
        low = [-1] * V       # Lowest discovery time reachable
        is_ap = [False] * V  # To mark articulation points
        self.timer = 0
        
        for i in range(V):
            if disc[i] == -1:
                self.dfs(i, -1, disc, low, is_ap, adj)
        
        # Collect marked points
        result = [i for i, val in enumerate(is_ap) if val]
        
        return result if result else [-1]

    def dfs(self, u, p, disc, low, is_ap, adj):
        disc[u] = low[u] = self.timer
        self.timer += 1
        children = 0
        
        for v in adj[u]:
            if v == p: continue # Don't go back to parent
            
            if disc[v] != -1:
                # Back-edge found: Update low value of u
                low[u] = min(low[u], disc[v])
            else:
                # Tree-edge: Child not visited
                children += 1
                self.dfs(v, u, disc, low, is_ap, adj)
                
                # Check low value of child
                low[u] = min(low[u], low[v])
                
                # AP Condition 1: Non-root node
                if p != -1 and low[v] >= disc[u]:
                    is_ap[u] = True
        
        # AP Condition 2: Root node with > 1 children
        if p == -1 and children > 1:
            is_ap[u] = True