class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        n = len(arr)
        # Result array initialized with -1
        res = [-1] * n
        # Stack to keep track of elements to the right
        stack = []
        
        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            curr = arr[i]
            
            # Pop elements from stack that are smaller than or equal to current
            while stack and stack[-1] <= curr:
                stack.pop()
            
            # If stack is not empty, the top is the next greater element
            if stack:
                res[i] = stack[-1]
            
            # Push current element onto stack
            stack.append(curr)
            
        return res