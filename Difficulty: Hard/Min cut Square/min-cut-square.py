class Solution:
    def minCut(self, a, b):
        self.res = a * b # Initial maximum result
        # Grid to keep track of filled cells
        board = [[False] * b for _ in range(a)]
        
        def solve(filled_count):
            # Pruning: if current count exceeds best found, stop
            if filled_count >= self.res:
                return

            # Find the first empty cell (top-to-bottom, left-to-right)
            r, c = -1, -1
            for i in range(a):
                for j in range(b):
                    if not board[i][j]:
                        r, c = i, j
                        break
                if r != -1: break
            
            # If no empty cell is found, we finished a valid partition
            if r == -1:
                self.res = min(self.res, filled_count)
                return

            # Try placing squares of different sizes at (r, c)
            # Size ranges from the largest possible down to 1
            for size in range(min(a - r, b - c), 0, -1):
                # Check if a square of this 'size' can fit
                can_fit = True
                for i in range(r, r + size):
                    for j in range(c, c + size):
                        if board[i][j]:
                            can_fit = False
                            break
                    if not can_fit: break
                
                if can_fit:
                    # Fill the square
                    for i in range(r, r + size):
                        for j in range(c, c + size):
                            board[i][j] = True
                    
                    solve(filled_count + 1)
                    
                    # Backtrack
                    for i in range(r, r + size):
                        for j in range(c, c + size):
                            board[i][j] = False

        solve(0)
        return self.res