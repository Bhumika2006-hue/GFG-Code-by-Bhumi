from collections import deque

class Solution:
    def shortCycle(self, V, edges):
        # 1. Build the adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        shortest = float('inf')
        
        # 2. Start BFS from every vertex
        for i in range(V):
            # dist[v] stores distance from vertex i to v
            dist = [float('inf')] * V
            parent = [-1] * V
            
            dist[i] = 0
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                
                for v in adj[u]:
                    if dist[v] == float('inf'):
                        # Neighbor not visited yet
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        queue.append(v)
                    elif parent[u] != v:
                        # Neighbor visited and not parent: Cycle found!
                        # Cycle length = dist[u] + dist[v] + 1
                        shortest = min(shortest, dist[u] + dist[v] + 1)
                        
                # Optimization: If we found a cycle of length 3, 
                # we can't do better in an undirected graph.
                if shortest == 3:
                    return 3
                    
        return shortest if shortest != float('inf') else -1