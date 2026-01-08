class Solution:
    def maxArea(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n = len(mat)
        m = len(mat[0])
        
        heights = [0] * m
        max_rectangle = 0
        
        for i in range(n):
            for j in range(m):
                # Update heights for the current row
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Find the largest rectangle in the histogram for this row
            max_rectangle = max(max_rectangle, self.largestHistogram(heights))
            
        return max_rectangle

    def largestHistogram(self, heights):
        stack = [] # Monotonic stack stores indices
        max_h_area = 0
        n = len(heights)
        
        for i in range(n + 1):
            # Use 0 as a sentinel to process all remaining bars in the stack
            curr_h = heights[i] if i < n else 0
            
            while stack and heights[stack[-1]] >= curr_h:
                h = heights[stack.pop()]
                # If stack is empty, width is i. Otherwise, i - index_of_prev_smaller - 1
                w = i if not stack else i - stack[-1] - 1
                max_h_area = max(max_h_area, h * w)
                
            stack.append(i)
            
        return max_h_area