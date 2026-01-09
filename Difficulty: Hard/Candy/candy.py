class Solution:
    def minCandy(self, arr):
        n = len(arr)
        if n == 0:
            return 0
            
        # Every child must have at least one candy
        candies = [1] * n
        
        # 1. Forward Pass: Check left neighbor
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                candies[i] = candies[i-1] + 1
        
        # 2. Backward Pass: Check right neighbor
        # We also keep track of total sum here to save an extra loop
        total_candies = candies[n-1]
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                # Take the max to satisfy both neighbors
                candies[i] = max(candies[i], candies[i+1] + 1)
            total_candies += candies[i]
            
        return total_candies