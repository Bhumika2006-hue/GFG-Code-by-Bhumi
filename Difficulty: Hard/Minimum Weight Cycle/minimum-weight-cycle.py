import heapq

class Solution:
    def findMinCycle(self, V, edges):
        # Build adjacency list: adj[u] = [(v, weight), ...]
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])
            
        min_cycle = float('inf')
        
        # Iterate over each edge to find the smallest cycle containing it
        for u, v, w in edges:
            # Dijkstra to find shortest path from u to v 
            # without using the direct edge (u, v)
            dist = self.dijkstra(u, v, V, adj, w)
            if dist != float('inf'):
                min_cycle = min(min_cycle, dist + w)
        
        return min_cycle if min_cycle != float('inf') else -1

    def dijkstra(self, start_node, target_node, V, adj, edge_weight):
        # distances initialized to infinity
        distances = [float('inf')] * V
        distances[start_node] = 0
        
        # priority queue stores (distance, current_node)
        pq = [(0, start_node)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > distances[u]:
                continue
            
            if u == target_node:
                return d
            
            for v, weight in adj[u]:
                # Skip the direct edge we are currently evaluating
                if (u == start_node and v == target_node and weight == edge_weight) or \
                   (u == target_node and v == start_node and weight == edge_weight):
                    continue
                
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(pq, (distances[v], v))
                    
        return distances[target_node]