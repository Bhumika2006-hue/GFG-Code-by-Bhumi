class Solution:
    def isMaxHeap(self, arr):
        n = len(arr)
        
        # Check for all non-leaf nodes
        for i in range(n // 2):
            
            # Left child
            left = 2 * i + 1
            if left < n and arr[i] < arr[left]:
                return False
            
            # Right child
            right = 2 * i + 2
            if right < n and arr[i] < arr[right]:
                return False
        
        return True