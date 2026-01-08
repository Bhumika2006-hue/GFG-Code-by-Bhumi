class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        # If start or end is blocked, no path is possible
        if not maze or maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []
            
        res = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        
        # Directions in lexicographical order: Down, Left, Right, Up
        # D: (1, 0), L: (0, -1), R: (0, 1), U: (-1, 0)
        directions = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]
        
        def solve(r, c, path):
            # Base Case: Reached destination
            if r == n - 1 and c == n - 1:
                res.append(path)
                return
            
            # Mark current cell as visited
            visited[r][c] = True
            
            for char, dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Safety check: Bounds, Not Blocked, Not Visited
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                    solve(nr, nc, path + char)
            
            # Backtrack: Unmark current cell for other path explorations
            visited[r][c] = False

        solve(0, 0, "")
        return res