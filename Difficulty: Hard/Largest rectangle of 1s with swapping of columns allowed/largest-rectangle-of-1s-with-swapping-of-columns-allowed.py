class Solution:
    def maxArea(self, mat, r, c):
        # Step 1: Compute the heights of 1s for each column
        # We use a 2D array to store heights to avoid modifying input
        hist = [[0] * c for _ in range(r)]
        
        for j in range(c):
            # First row initialization
            hist[0][j] = 1 if mat[0][j] == 1 else 0
            # Subsequent rows
            for i in range(1, r):
                if mat[i][j] == 1:
                    hist[i][j] = hist[i-1][j] + 1
                else:
                    hist[i][j] = 0
        
        max_area = 0
        
        # Step 2: For each row, sort heights and find max rectangle
        for i in range(r):
            # Get the heights for the current row and sort them descending
            curr_row = sorted(hist[i], reverse=True)
            
            for j in range(c):
                # Area = height of the j-th column * number of columns (j+1)
                area = curr_row[j] * (j + 1)
                if area > max_area:
                    max_area = area
                    
        return max_area