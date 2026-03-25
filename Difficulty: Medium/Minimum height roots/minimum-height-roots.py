from collections import deque

class Solution:
    def minHeightRoot(self, V, edges):
        if V == 1:
            return [0]
        
        # Build graph
        adj = [[] for _ in range(V)]
        degree = [0] * V
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Initialize leaves
        q = deque()
        for i in range(V):
            if degree[i] == 1:
                q.append(i)
        
        remaining = V
        
        # Remove leaves layer by layer
        while remaining > 2:
            size = len(q)
            remaining -= size
            
            for _ in range(size):
                leaf = q.popleft()
                
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        q.append(neighbor)
        
        return list(q)