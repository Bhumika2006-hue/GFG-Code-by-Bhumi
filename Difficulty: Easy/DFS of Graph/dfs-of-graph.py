class Solution:
    def dfs(self, adj):
        visited = [False] * len(adj)
        result = []
        
        def dfsUtil(u):
            visited[u] = True
            result.append(u)
            for v in adj[u]:
                if not visited[v]:
                    dfsUtil(v)
        
        dfsUtil(0)
        return result
