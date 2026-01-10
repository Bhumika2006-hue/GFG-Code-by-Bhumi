from typing import List

class Solution:
    def zeroSumSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
            
        rows = len(mat)
        cols = len(mat[0])
        max_area = 0
        
        # Fixing the left column
        for l in range(cols):
            # temp stores the row-wise sum between column l and current r
            row_sums = [0] * rows
            
            # Fixing the right column
            for r in range(l, cols):
                for i in range(rows):
                    row_sums[i] += mat[i][r]
                
                # Find the longest subarray with sum 0 in row_sums
                # Using Prefix Sum + Hash Map
                prefix_map = {0: -1}
                current_sum = 0
                
                for i in range(rows):
                    current_sum += row_sums[i]
                    
                    if current_sum in prefix_map:
                        # length = (current index - first index where this sum was seen)
                        height = i - prefix_map[current_sum]
                        width = (r - l + 1)
                        max_area = max(max_area, height * width)
                    else:
                        prefix_map[current_sum] = i
                        
        return max_area