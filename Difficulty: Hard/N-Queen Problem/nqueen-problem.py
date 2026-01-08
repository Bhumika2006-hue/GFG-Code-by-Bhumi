class Solution:
    def nQueen(self, n):
        res = []
        # Track occupied columns and diagonals
        cols = [False] * (n + 1)
        diag1 = [False] * (2 * n + 1) # r - c + n
        diag2 = [False] * (2 * n + 1) # r + c
        
        def solve(row, current_board):
            # Base Case: All queens placed
            if row > n:
                res.append(list(current_board))
                return
            
            for col in range(1, n + 1):
                # Check if the column or diagonals are under attack
                if not cols[col] and not diag1[row - col + n] and not diag2[row + col]:
                    # Place Queen
                    cols[col] = diag1[row - col + n] = diag2[row + col] = True
                    current_board.append(col)
                    
                    # Recurse to the next row
                    solve(row + 1, current_board)
                    
                    # Backtrack: Remove Queen and unmark constraints
                    current_board.pop()
                    cols[col] = diag1[row - col + n] = diag2[row + col] = False
                    
        solve(1, [])
        return res