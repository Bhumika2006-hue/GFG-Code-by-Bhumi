import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(10**6)

class Solution:
    def criticalConnections(self, v, adj):
        # disc[i]: discovery time of node i
        # low[i]: lowest discovery time reachable from node i
        disc = [-1] * v
        low = [-1] * v
        bridges = []
        self.timer = 0
        
        def dfs(u, p=-1):
            disc[u] = low[u] = self.timer
            self.timer += 1
            
            for v_neighbor in adj[u]:
                if v_neighbor == p:
                    continue
                
                if disc[v_neighbor] == -1:  # If neighbor is not visited
                    dfs(v_neighbor, u)
                    low[u] = min(low[u], low[v_neighbor])
                    
                    # Check the bridge condition
                    if low[v_neighbor] > disc[u]:
                        # Ensure the edge is stored in sorted order as requested
                        bridges.append(sorted([u, v_neighbor]))
                else:
                    # Update low value for back-edge
                    low[u] = min(low[u], disc[v_neighbor])
        
        # Since the graph is connected, one DFS starting from node 0 is enough
        dfs(0)
        
        # Return bridges sorted lexicographically
        bridges.sort()
        return bridges