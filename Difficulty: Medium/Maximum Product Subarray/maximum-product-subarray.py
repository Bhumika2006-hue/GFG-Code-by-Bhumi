class Solution:
    # Function to find maximum product subarray
    def maxProduct(self, arr):
        n = len(arr)
        max_prod = float('-inf')
        
        prefix = 1
        suffix = 1
        
        for i in range(n):
            # If prefix product becomes 0, reset it to 1
            if prefix == 0:
                prefix = 1
            # If suffix product becomes 0, reset it to 1
            if suffix == 0:
                suffix = 1
                
            # Calculate prefix from left
            prefix *= arr[i]
            # Calculate suffix from right
            suffix *= arr[n - 1 - i]
            
            # Keep track of the maximum value found so far
            max_prod = max(max_prod, max(prefix, suffix))
            
        return max_prod