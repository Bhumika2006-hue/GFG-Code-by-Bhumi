import heapq

class Solution:
    def minimumCostPath(self, grid):
        n = len(grid)
        
        # Distance matrix to store the minimum cost to reach each cell
        # Initialize with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Priority Queue for Dijkstra: (current_total_cost, row, col)
        # Starting point is the top-left cell
        pq = [(grid[0][0], 0, 0)]
        dist[0][0] = grid[0][0]
        
        # Possible directions: Down, Up, Right, Left
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        
        while pq:
            curr_cost, r, c = heapq.heappop(pq)
            
            # If we reached the bottom-right cell, return the cost
            if r == n - 1 and c == n - 1:
                return curr_cost
                
            # If we find a cost in the heap that is already worse than 
            # our best known distance, skip it
            if curr_cost > dist[r][c]:
                continue
            
            # Check all 4 neighbors
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                
                # Boundary check
                if 0 <= nr < n and 0 <= nc < n:
                    new_cost = curr_cost + grid[nr][nc]
                    
                    # If this path to the neighbor is cheaper, update it
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))
                        
        return dist[n-1][n-1]