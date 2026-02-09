class Solution:
    def findKRotation(self, arr):
        low, high = 0, len(arr) - 1
        
        while low <= high:
            # If already sorted
            if arr[low] <= arr[high]:
                return low
            
            mid = (low + high) // 2
            next_idx = (mid + 1) % len(arr)
            prev_idx = (mid - 1 + len(arr)) % len(arr)
            
            # Check if mid is minimum
            if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
                return mid
            
            # Decide which side to go
            if arr[mid] >= arr[low]:
                low = mid + 1
            else:
                high = mid - 1
        
        return 0
