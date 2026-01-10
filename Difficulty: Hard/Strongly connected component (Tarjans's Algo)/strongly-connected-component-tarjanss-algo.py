import sys

# Increase recursion depth for large graphs
sys.setrecursionlimit(10**6)

class Solution:
    def tarjans(self, V, adj):
        # disc: time of discovery for each node
        # low: lowest discovery time reachable from node
        # stack_member: boolean array to check if node is currently in stack
        disc = [-1] * V
        low = [-1] * V
        stack_member = [False] * V
        st = []
        result = []
        self.timer = 0
        
        def findSCC(u):
            disc[u] = low[u] = self.timer
            self.timer += 1
            st.append(u)
            stack_member[u] = True
            
            for v in adj[u]:
                # If v is not visited, recurse
                if disc[v] == -1:
                    findSCC(v)
                    low[u] = min(low[u], low[v])
                # If v is in stack, it's a back-edge to a node in the current SCC
                elif stack_member[v]:
                    low[u] = min(low[u], disc[v])
            
            # If u is the head of an SCC
            if low[u] == disc[u]:
                current_scc = []
                while True:
                    w = st.pop()
                    stack_member[w] = False
                    current_scc.append(w)
                    if u == w:
                        break
                # Requirement: Sort the individual component
                current_scc.sort()
                result.append(current_scc)

        # Run DFS for every unvisited node
        for i in range(V):
            if disc[i] == -1:
                findSCC(i)
        
        # Requirement: Sort the list of SCCs lexicographically
        result.sort()
        return result