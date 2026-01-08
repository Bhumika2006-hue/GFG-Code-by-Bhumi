class Solution:
    def peakElement(self, arr):
        n = len(arr)
        
        # Binary search range
        low = 0
        high = n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is a peak
            # 1. Compare with left neighbor (or check if it's the first element)
            # 2. Compare with right neighbor (or check if it's the last element)
            left_ok = (mid == 0 or arr[mid] > arr[mid - 1])
            right_ok = (mid == n - 1 or arr[mid] > arr[mid + 1])
            
            if left_ok and right_ok:
                return mid
            
            # If the right neighbor is greater, there must be a peak on the right
            if mid < n - 1 and arr[mid + 1] > arr[mid]:
                low = mid + 1
            # Otherwise, there must be a peak on the left
            else:
                high = mid - 1
                
        return -1 # Should not reach here based on problem constraints