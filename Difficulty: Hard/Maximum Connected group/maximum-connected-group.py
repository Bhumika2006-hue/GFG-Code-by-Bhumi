from typing import List

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_sizes = {}
        island_id = 2  # Start ID from 2 because 0 and 1 are already used
        
        # Helper to get valid neighbors
        def get_neighbors(r, c):
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc

        # 1. BFS/DFS to find all connected components (islands)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = 0
                    stack = [(r, c)]
                    grid[r][c] = island_id
                    while stack:
                        curr_r, curr_c = stack.pop()
                        size += 1
                        for nr, nc in get_neighbors(curr_r, curr_c):
                            if grid[nr][nc] == 1:
                                grid[nr][nc] = island_id
                                stack.append((nr, nc))
                    island_sizes[island_id] = size
                    island_id += 1

        # If the grid is all 1s, return the full area
        if not island_sizes:
            return 1 if n > 0 else 0
        
        # Max size if we don't flip anything, or flip a 0 next to an island
        max_area = max(island_sizes.values())
        
        # 2. Iterate through every 0 to find the best flip
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighboring_islands = set()
                    for nr, nc in get_neighbors(r, c):
                        if grid[nr][nc] > 1:
                            neighboring_islands.add(grid[nr][nc])
                    
                    # Current 0 + sum of unique neighboring island areas
                    potential_area = 1 + sum(island_sizes[i_id] for i_id in neighboring_islands)
                    max_area = max(max_area, potential_area)
                    
        return max_area
        
