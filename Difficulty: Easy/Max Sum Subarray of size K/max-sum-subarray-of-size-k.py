class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        if n < k:
            return 0
        
        # 1. Compute the sum of the first window
        current_sum = sum(arr[:k])
        max_sum = current_sum
        
        # 2. Slide the window across the rest of the array
        for i in range(k, n):
            # Add the element entering the window (arr[i])
            # Subtract the element leaving the window (arr[i - k])
            current_sum += arr[i] - arr[i - k]
            
            # Update max_sum
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum            
        