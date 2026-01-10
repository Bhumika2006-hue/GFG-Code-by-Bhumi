from collections import deque

class Solution:
    def shotestPath(self, mat, n, m, k):
        # Initial state: (row, col, remaining_k, steps)
        queue = deque([(0, 0, k, 0)])
        
        # visited[r][c] stores the maximum remaining 'k' seen so far for that cell
        # Initialize with -1 to indicate the cell hasn't been visited
        visited = [[-1 for _ in range(m)] for _ in range(n)]
        visited[0][0] = k
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c, k_rem, steps = queue.popleft()
            
            # If we reached the target
            if r == n - 1 and c == m - 1:
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Boundary check
                if 0 <= nr < n and 0 <= nc < m:
                    new_k = k_rem - mat[nr][nc]
                    
                    # If we have enough k to pass and haven't seen this cell with better k
                    if new_k >= 0 and visited[nr][nc] < new_k:
                        visited[nr][nc] = new_k
                        queue.append((nr, nc, new_k, steps + 1))
                        
        return -1