class Solution:
    def avoidExlosion(self, mix, n, danger, m):
        # parent array for DSU
        parent = list(range(n + 1))
        
        # Find with path compression
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        # Union operation
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
        
        ans = []
        for x, y in mix:
            rootX = find(x)
            rootY = find(y)
            
            if rootX == rootY:
                ans.append("Yes")
                continue
                
            can_mix = True
            # Check every danger pair against the current roots
            for p, q in danger:
                rootP = find(p)
                rootQ = find(q)
                
                # If merging rootX and rootY connects p and q
                if (rootP == rootX and rootQ == rootY) or (rootP == rootY and rootQ == rootX):
                    can_mix = False
                    break
            
            if can_mix:
                union(rootX, rootY)
                ans.append("Yes")
            else:
                ans.append("No")
                
        return ans