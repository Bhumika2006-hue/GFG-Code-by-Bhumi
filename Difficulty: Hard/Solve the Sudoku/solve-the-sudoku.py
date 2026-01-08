class Solution:
    def solveSudoku(self, mat):
        self.solve(mat)
        
    def solve(self, mat):
        for r in range(9):
            for c in range(9):
                if mat[r][c] == 0:
                    for num in range(1, 10):
                        if self.is_valid(mat, r, c, num):
                            mat[r][c] = num
                            
                            if self.solve(mat):
                                return True
                            
                            # Backtrack
                            mat[r][c] = 0
                    return False
        return True

    def is_valid(self, mat, r, c, num):
        # Check row and column
        for i in range(9):
            if mat[r][i] == num or mat[i][c] == num:
                return False
        
        # Check 3x3 box
        # start_row and start_col represent the top-left of the 3x3 subgrid
        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                if mat[start_row + i][start_col + j] == num:
                    return False
                    
        return True