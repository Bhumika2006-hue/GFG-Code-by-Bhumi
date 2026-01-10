class Solution:
    def recreationalSpot(self, arr, n):
        if n < 3:
            return False
        
        # Step 1: Precompute the minimum element to the left of each index
        # min_prefix[i] is the smallest value in arr[0...i-1]
        min_prefix = [0] * n
        min_prefix[0] = arr[0]
        for i in range(1, n):
            min_prefix[i] = min(min_prefix[i-1], arr[i])
            
        # Step 2: Use a stack to find the '2' (arr[k]) 
        # while iterating backwards to pick the '3' (arr[j])
        stack = []
        
        # Iterate from right to left
        for j in range(n - 1, -1, -1):
            # We only care if the current building is taller than the 
            # minimum building to its left (potential arr[i])
            if arr[j] > min_prefix[j]:
                
                # Maintain the stack: remove elements smaller than or 
                # equal to the minimum prefix because they can't be our '2'
                while stack and stack[-1] <= min_prefix[j]:
                    stack.pop()
                
                # If we find an element in the stack that is smaller than 
                # the current peak arr[j], we've found our 1-3-2 pattern!
                # (Since stack[-1] > min_prefix[j] is already guaranteed)
                if stack and stack[-1] < arr[j]:
                    return True
                
                stack.append(arr[j])
                
        return False