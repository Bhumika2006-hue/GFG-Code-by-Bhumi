class Solution:
    def medianOf2(self, a, b):
        n = len(a)
        low = 0
        high = n
        
        while low <= high:
            # Partition index for array a
            i = (low + high) // 2
            # Partition index for array b such that i + j = n
            j = n - i
            
            # Boundary conditions: if i is 0, there's no element on the left of a
            # If i is n, there's no element on the right of a
            a_left = a[i-1] if i > 0 else float('-inf')
            a_right = a[i] if i < n else float('inf')
            
            b_left = b[j-1] if j > 0 else float('-inf')
            b_right = b[j] if j < n else float('inf')
            
            # Check if we found the correct partition
            if a_left <= b_right and b_left <= a_right:
                # The median is the average of the max of lefts and min of rights
                left_max = max(a_left, b_left)
                right_min = min(a_right, b_right)
                
                # Use float for division to handle .5 cases
                return (left_max + right_min) / 2.0
            
            elif a_left > b_right:
                # Too many elements from a on the left, move left
                high = i - 1
            else:
                # Too many elements from b on the left, move right
                low = i + 1
                
        return 0.0