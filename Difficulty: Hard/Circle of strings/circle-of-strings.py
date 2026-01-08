class Solution:
    def isCircle(self, arr):
        # 26 possible characters 'a' to 'z'
        in_degree = [0] * 26
        out_degree = [0] * 26
        adj = [[] for _ in range(26)]
        
        nodes_present = set()
        
        for s in arr:
            u = ord(s[0]) - ord('a')
            v = ord(s[-1]) - ord('a')
            
            out_degree[u] += 1
            in_degree[v] += 1
            adj[u].append(v)
            nodes_present.add(u)
            nodes_present.add(v)
            
        # Condition 1: Check if In-degree equals Out-degree for all characters
        for i in range(26):
            if in_degree[i] != out_degree[i]:
                return 0
        
        # Condition 2: Check if all edges belong to a single connected component
        # We start a BFS/DFS from the first character of the first string
        start_node = ord(arr[0][0]) - ord('a')
        visited = [False] * 26
        
        self.dfs(start_node, adj, visited)
        
        # All characters that appear in strings must have been visited
        for node in nodes_present:
            if not visited[node]:
                return 0
                
        return 1

    def dfs(self, u, adj, visited):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                self.dfs(v, adj, visited)