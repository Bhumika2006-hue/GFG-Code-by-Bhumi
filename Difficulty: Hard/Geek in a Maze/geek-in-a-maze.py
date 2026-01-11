from collections import deque

class Solution:
    def numberOfCells(self, n, m, r, c, u, d, mat):
        # If the starting cell is an obstacle, no cells can be visited
        if mat[r][c] == '#':
            return 0
        
        # dists[i][j] stores (remaining_up, remaining_down) for cell (i, j)
        # We initialize with -1 to indicate the cell hasn't been visited optimally
        visited_up = [[-1] * m for _ in range(n)]
        visited_down = [[-1] * m for _ in range(n)]
        
        # Deque stores: (row, col, remaining_up, remaining_down)
        dq = deque([(r, c, u, d)])
        visited_up[r][c] = u
        visited_down[r][c] = d
        
        count = 0
        
        while dq:
            curr_r, curr_c, curr_u, curr_d = dq.popleft()
            
            # Directions: Up, Down, Left, Right
            # We process Left/Right first in the logic or use deque priorities
            for dr, dc, move_type in [(0, 1, 'L/R'), (0, -1, 'L/R'), (-1, 0, 'U'), (1, 0, 'D')]:
                nr, nc = curr_r + dr, curr_c + dc
                
                # Boundary and obstacle check
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == '.':
                    next_u, next_d = curr_u, curr_d
                    
                    if move_type == 'U':
                        next_u -= 1
                    elif move_type == 'D':
                        next_d -= 1
                    
                    # Check if moves are still available and if this path is better
                    if next_u >= 0 and next_d >= 0:
                        if next_u > visited_up[nr][nc] or next_d > visited_down[nr][nc]:
                            visited_up[nr][nc] = next_u
                            visited_down[nr][nc] = next_d
                            
                            # Add to front if it's a "free" side move, else to back
                            if move_type == 'L/R':
                                dq.appendleft((nr, nc, next_u, next_d))
                            else:
                                dq.append((nr, nc, next_u, next_d))
        
        # Count all cells that were visited
        for i in range(n):
            for j in range(m):
                if visited_up[i][j] != -1:
                    count += 1
                    
        return count