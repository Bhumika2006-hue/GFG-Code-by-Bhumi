import collections

class Solution:
    def assignmentProblem(self, Arr, N):
        # Reshape the flat Arr into an N x N cost matrix
        matrix = []
        for i in range(N):
            matrix.append(Arr[i*N : (i+1)*N])
            
        # Hungarian Algorithm / Min-cost matching in bipartite graph
        # Using a BFS-based augmenting path approach (Kuhn-Munkres)
        
        u = [0] * (N + 1) # Potential for rows
        v = [0] * (N + 1) # Potential for columns
        p = [0] * (N + 1) # Matching: p[j] = i means job j is assigned to person i
        way = [0] * (N + 1)
        
        for i in range(1, N + 1):
            p[0] = i
            j0 = 0
            minv = [float('inf')] * (N + 1)
            used = [False] * (N + 1)
            
            while True:
                used[j0] = True
                i0 = p[j0]
                delta = float('inf')
                j1 = 0
                for j in range(1, N + 1):
                    if not used[j]:
                        # Calculate current reduced cost
                        cur = matrix[i0-1][j-1] - u[i0] - v[j]
                        if cur < minv[j]:
                            minv[j] = cur
                            way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]
                            j1 = j
                
                for j in range(N + 1):
                    if used[j]:
                        u[p[j]] += delta
                        v[j] -= delta
                    else:
                        minv[j] -= delta
                
                j0 = j1
                if p[j0] == 0:
                    break
            
            while True:
                j1 = way[j0]
                p[j0] = p[j1]
                j0 = j1
                if j0 == 0:
                    break
                    
        # The total minimum cost is stored in -v[0] in this implementation
        return -v[0]