class Solution:
    def maxRectSum(self, mat):
        if not mat or not mat[0]:
            return 0
            
        rows = len(mat)
        cols = len(mat[0])
        max_sum = float('-inf')
        
        # Kadane's algorithm helper
        def kadane(arr):
            max_end_here = 0
            max_so_far = float('-inf')
            for x in arr:
                max_end_here += x
                if max_so_far < max_end_here:
                    max_so_far = max_end_here
                if max_end_here < 0:
                    max_end_here = 0
            return max_so_far

        # Try every possible combination of left and right columns
        for left in range(cols):
            # temp stores the row sums for the current left-right boundary
            temp = [0] * rows
            for right in range(left, cols):
                for i in range(rows):
                    temp[i] += mat[i][right]
                
                # Apply Kadane's on the compressed 1D row sums
                current_max = kadane(temp)
                max_sum = max(max_sum, current_max)
                
        return max_sum