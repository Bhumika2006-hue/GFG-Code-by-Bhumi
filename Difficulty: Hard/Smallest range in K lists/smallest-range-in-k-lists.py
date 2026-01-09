import heapq

class Solution:
    def findSmallestRange(self, mat):
        n = len(mat)
        k = len(mat[0])
        
        # min_heap will store (value, row_index, column_index)
        min_heap = []
        curr_max = float('-inf')
        
        # 1. Initialize heap with the first element of each row
        for i in range(n):
            val = mat[i][0]
            heapq.heappush(min_heap, (val, i, 0))
            curr_max = max(curr_max, val)
        
        # Initial range results
        start, end = min_heap[0][0], curr_max
        
        while len(min_heap) == n:
            curr_min, r, c = heapq.heappop(min_heap)
            
            # 2. Update the smallest range found so far
            if curr_max - curr_min < end - start:
                start, end = curr_min, curr_max
            
            # 3. If there's a next element in the same row, add it to heap
            if c + 1 < k:
                next_val = mat[r][c + 1]
                heapq.heappush(min_heap, (next_val, r, c + 1))
                curr_max = max(curr_max, next_val)
            else:
                # One list is exhausted, cannot form a range with all lists anymore
                break
                
        return [start, end]