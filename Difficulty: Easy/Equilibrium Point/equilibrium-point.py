class Solution:
    # Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(len(arr)):
            # Calculate right sum by subtracting left_sum and current element
            right_sum = total_sum - left_sum - arr[i]
            
            if left_sum == right_sum:
                return i
            
            # Update left_sum for the next index
            left_sum += arr[i]
            
        return -1