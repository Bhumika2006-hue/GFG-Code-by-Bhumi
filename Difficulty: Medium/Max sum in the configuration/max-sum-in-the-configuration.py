class Solution:
    def maxSum(self, arr):
        n = len(arr)
        
        # Compute arrSum and R0
        arrSum = sum(arr)
        currVal = 0
        for i in range(n):
            currVal += i * arr[i]
        
        maxVal = currVal
        
        # Compute values for all rotations
        for i in range(1, n):
            currVal = currVal + arrSum - n * arr[n - i]
            maxVal = max(maxVal, currVal)
        
        return maxVal
