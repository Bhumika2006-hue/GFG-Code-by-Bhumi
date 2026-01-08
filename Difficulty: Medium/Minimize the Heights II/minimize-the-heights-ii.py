class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        
        # Step 1: Sort the array
        arr.sort()
        
        # Initial difference between max and min heights
        ans = arr[n-1] - arr[0]
        
        # Step 2: Iterate through the array to find the best split point
        for i in range(n - 1):
            # Calculate the potential new maximum and minimum
            # Smallest becomes either the first element + k or the next element - k
            mini = min(arr[0] + k, arr[i+1] - k)
            
            # Largest becomes either the last element - k or the current element + k
            maxi = max(arr[n-1] - k, arr[i] + k)
            
            # Rule: Resultant height cannot be negative
            if mini < 0:
                continue
            
            # Update the global minimum difference
            ans = min(ans, maxi - mini)
            
        return ans