from typing import List
import collections

class Solution:
    def maximumDistance(self, v : int, e : int, src : int, edges : List[List[int]]) -> List[int]:
        # 1. Build adjacency list
        adj = collections.defaultdict(list)
        in_degree = [0] * v
        for u, node_v, w in edges:
            adj[u].append((node_v, w))
            in_degree[node_v] += 1
            
        # 2. Kahn's Algorithm for Topological Sort
        topo_order = []
        queue = collections.deque([i for i in range(v) if in_degree[i] == 0])
        
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for neighbor, weight in adj[u]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 3. Initialize distances
        # We use a specific very small value for unreachability
        # Many platforms use -1e9 or similar to represent INF for longest path
        INF_VAL = -float('inf')
        dist = [INF_VAL] * v
        dist[src] = 0
        
        # 4. Relax edges in topological order
        for u in topo_order:
            if dist[u] != INF_VAL:
                for neighbor, weight in adj[u]:
                    if dist[u] + weight > dist[neighbor]:
                        dist[neighbor] = dist[u] + weight
        
        # 5. Format output
        # To match the "INF" requirement, we return the string "INF" 
        # or a value the driver recognizes. Based on your error log, 
        # the driver replaces a specific large negative value with "INF".
        # Let's use "INF" as a string if the return type allows, 
        # otherwise use a standard placeholder.
        
        res = []
        for d in dist:
            if d == INF_VAL:
                res.append("INF")
            else:
                res.append(int(d))
                
        return res