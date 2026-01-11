import sys
sys.setrecursionlimit(10**6)

class Solution:
    def captainAmerica(self, n, gates):
        adj = [[] for _ in range(n + 1)]
        rev_adj = [[] for _ in range(n + 1)]
        for u, v in gates:
            adj[u].append(v)
            rev_adj[v].append(u)

        stack = []
        visited = [False] * (n + 1)

        # First pass: Fill stack with finishing times
        def dfs1(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs1(v)
            stack.append(u)

        # Second pass: Extract SCCs
        def dfs2(u, component):
            visited[u] = True
            component.append(u)
            for v in rev_adj[u]:
                if not visited[v]:
                    dfs2(v, component)

        for i in range(1, n + 1):
            if not visited[i]:
                dfs1(i)

        visited = [False] * (n + 1)
        sccs = []
        while stack:
            u = stack.pop()
            if not visited[u]:
                comp = []
                dfs2(u, comp)
                sccs.append(comp)

        # Map each node to its SCC index
        node_to_scc = [0] * (n + 1)
        for idx, comp in enumerate(sccs):
            for node in comp:
                node_to_scc[node] = idx

        # Calculate out-degree of each SCC
        scc_out_degree = [0] * len(sccs)
        for u, v in gates:
            if node_to_scc[u] != node_to_scc[v]:
                scc_out_degree[node_to_scc[u]] += 1

        # Count SCCs with out-degree zero
        zero_out_indices = [i for i, deg in enumerate(scc_out_degree) if deg == 0]

        # If more than one SCC has out-degree 0, they can't reach each other
        if len(zero_out_indices) != 1:
            return 0
        
        # Return the number of nodes in that unique terminal SCC
        return len(sccs[zero_out_indices[0]])