from bisect import bisect_right

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        # The range of potential median values
        low = float('inf')
        high = float('-inf')
        
        for i in range(n):
            low = min(low, mat[i][0])
            high = max(high, mat[i][m-1])
            
        # We need more than half the elements to be <= median
        desired_count = (n * m) // 2
        
        ans = low
        while low <= high:
            mid = (low + high) // 2
            
            # Count elements <= mid in the entire matrix
            count = 0
            for i in range(n):
                # bisect_right finds the position where 'mid' could be inserted 
                # while maintaining order, effectively counting elements <= mid.
                count += bisect_right(mat[i], mid)
                
            if count <= desired_count:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
                
        return ans