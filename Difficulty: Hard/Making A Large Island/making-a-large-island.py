class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        island_sizes = {}
        island_id = 2
        
        def get_neighbors(r, c):
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc

        # Step 1: Label existing islands and store their sizes
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

        # If no islands exist, we can create one of size 1
        # If the grid is all 1s, the largest island is n*n
        if not island_sizes:
            return 1
        
        max_area = max(island_sizes.values())
        if max_area < n * n:
            # We can at least add 1 to an existing island by flipping a 0
            max_area += 0 

        # Step 2: Try flipping each 0 to connect adjacent islands
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbor_ids = set()
                    for nr, nc in get_neighbors(r, c):
                        if grid[nr][nc] > 1:
                            neighbor_ids.add(grid[nr][nc])
                    
                    # Size = the 1 we just added + sizes of all unique surrounding islands
                    current_potential = 1 + sum(island_sizes[i_id] for i_id in neighbor_ids)
                    max_area = max(max_area, current_potential)
                    
        return min(max_area, n * n)