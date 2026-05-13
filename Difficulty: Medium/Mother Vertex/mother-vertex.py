class Solution:
    def findMotherVertex(self, V, edges):
        from collections import defaultdict
        
        # Step 1: Build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        visited = [False] * V
        
        # DFS function
        def dfs(v):
            visited[v] = True
            for nei in graph[v]:
                if not visited[nei]:
                    dfs(nei)
        
        # Step 2: Find candidate
        last_v = 0
        for i in range(V):
            if not visited[i]:
                dfs(i)
                last_v = i
        
        # Step 3: Verify candidate
        visited = [False] * V
        dfs(last_v)
        
        if all(visited):
            return last_v
        return -1