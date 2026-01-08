class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        current_sum = 0
        left = 0
        
        # Iterate through the array using 'right' as the end of the window
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window from the left if current_sum exceeds target
            # Ensure left <= right to handle cases where target is 0 or small
            while current_sum > target and left < right:
                current_sum -= arr[left]
                left += 1
            
            # Check if we found the target
            if current_sum == target:
                # Return 1-based indices
                return [left + 1, right + 1]
                
        # If no subarray is found
        return [-1]

# Example usage:
# sol = Solution()
# print(sol.subarraySum([1, 2, 3, 7, 5], 12)) # Output: [2, 4]