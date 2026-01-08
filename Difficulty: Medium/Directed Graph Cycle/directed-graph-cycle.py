from collections import deque

class Solution:
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, edges):
        # 1. Build adjacency list and in-degree array
        adj = [[] for _ in range(V)]
        in_degree = [0] * V
        
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
            
        # 2. Add all vertices with 0 in-degree to the queue
        queue = deque()
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
                
        # 3. Process the queue
        count = 0
        while queue:
            u = queue.popleft()
            count += 1
            
            # Reduce in-degree of all neighbors
            for v in adj[u]:
                in_degree[v] -= 1
                # If in-degree becomes 0, add to queue
                if in_degree[v] == 0:
                    queue.append(v)
        
        # 4. If processed count != total vertices, there's a cycle
        # If count == V, it's a DAG (No cycle)
        return count != V