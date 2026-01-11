from collections import deque

class Solution:
    def findMaxFlow(self, N, M, Edges):
        # Initialize residual capacity matrix
        # Note: N+1 because vertices are 1-indexed
        capacity = [[0] * (N + 1) for _ in range(N + 1)]
        adj = [[] for _ in range(N + 1)]
        
        for u, v, w in Edges:
            # The problem mentions undirected edges, which in flow networks 
            # effectively means both directions can carry capacity.
            # If multiple edges exist between same nodes, sum their capacities.
            capacity[u][v] += w
            capacity[v][u] += w
            adj[u].append(v)
            adj[v].append(u)
            
        source = 1
        sink = N
        max_flow = 0
        
        while True:
            # BFS to find augmenting path
            parent = [-1] * (N + 1)
            queue = deque([source])
            parent[source] = source
            
            while queue:
                curr = queue.popleft()
                if curr == sink:
                    break
                for nxt in adj[curr]:
                    if parent[nxt] == -1 and capacity[curr][nxt] > 0:
                        parent[nxt] = curr
                        queue.append(nxt)
                else:
                    continue
                break
            else:
                # No augmenting path found
                break
                
            # Find bottleneck capacity
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, capacity[parent[s]][s])
                s = parent[s]
                
            # Update residual capacities
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                capacity[u][v] -= path_flow
                capacity[v][u] += path_flow
                v = parent[v]
                
        return max_flow