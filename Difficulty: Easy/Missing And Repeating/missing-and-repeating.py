class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        # Create a frequency array of size n+1
        count = [0] * (n + 1)
        
        for num in arr:
            count[num] += 1
            
        repeating = -1
        missing = -1
        
        # Check counts to identify the two numbers
        for i in range(1, n + 1):
            if count[i] == 2:
                repeating = i
            elif count[i] == 0:
                missing = i
                
            # Optimization: If both found, break early
            if repeating != -1 and missing != -1:
                break
                
        return [repeating, missing]