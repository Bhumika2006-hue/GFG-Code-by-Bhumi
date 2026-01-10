class Solution:
    def maximumWeight(self, n, edges, q, queries):
        # DSU structure to keep track of component sizes and path counts
        parent = list(range(n + 1))
        size = [1] * (n + 1)
        self.total_paths = 0

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                # Number of new paths formed by connecting these components
                self.total_paths += size[root_i] * size[root_j]
                
                # Standard Union by Size
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i
                parent[root_j] = root_i
                size[root_i] += size[root_j]

        # Sort edges by weight
        edges.sort(key=lambda x: x[2])
        
        # Sort queries while keeping track of original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        ans = [0] * q
        edge_idx = 0
        
        for original_idx, x in sorted_queries:
            # Add all edges with weight <= current query x
            while edge_idx < len(edges) and edges[edge_idx][2] <= x:
                u, v, w = edges[edge_idx]
                union(u, v)
                edge_idx += 1
            
            # Store the result for the original query index
            ans[original_idx] = self.total_paths
            
        return ans