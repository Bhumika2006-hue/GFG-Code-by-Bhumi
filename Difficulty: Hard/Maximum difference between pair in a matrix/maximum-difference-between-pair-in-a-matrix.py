from typing import List

class Solution:
    def findMaxValue(self, n : int, mat : List[List[int]]) -> int:
        # min_mat[i][j] will store the minimum value in the submatrix
        # from (0,0) to (i,j)
        min_mat = [[0] * n for _ in range(n)]
        
        # Initialize the first element
        min_mat[0][0] = mat[0][0]
        
        # Precompute the first row of min_mat
        for j in range(1, n):
            min_mat[0][j] = min(mat[0][j], min_mat[0][j-1])
            
        # Precompute the first column of min_mat
        for i in range(1, n):
            min_mat[i][0] = min(mat[i][0], min_mat[i-1][0])
            
        max_diff = float('-inf')
        
        # Start from (1,1) because we need c > a and d > b
        # a, b must be at least one row/column behind c, d
        for i in range(1, n):
            for j in range(1, n):
                # Calculate difference with the minimum found in the 
                # strictly top-left submatrix mat[0...i-1][0...j-1]
                current_diff = mat[i][j] - min_mat[i-1][j-1]
                if current_diff > max_diff:
                    max_diff = current_diff
                
                # Update min_mat for future cells
                min_mat[i][j] = min(mat[i][j], min_mat[i-1][j], min_mat[i][j-1])
                
        return max_diff