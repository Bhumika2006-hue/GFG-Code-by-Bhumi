class Solution:
    # Changed 'A' to 'a' in Subarray to match the driver code
    def maxSubarraySum(self, arr):
        # Initialize with the first element
        max_so_far = arr[0]
        curr_max = arr[0]
        
        for i in range(1, len(arr)):
            # Kadane's logic: 
            # Should we extend the existing subarray or start fresh?
            curr_max = max(arr[i], curr_max + arr[i])
            
            # Update the global best sum found so far
            if curr_max > max_so_far:
                max_so_far = curr_max
                
        return max_so_far