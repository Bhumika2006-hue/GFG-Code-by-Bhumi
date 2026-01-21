class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        span = [0] * n
        stack = [] # Stores indices of the prices
        
        for i in range(n):
            # Pop elements from stack while stack is not empty 
            # and current price is greater than price at stack top
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            # If stack is empty, current element is greater than all previous elements
            if not stack:
                span[i] = i + 1
            else:
                # Span is the difference between current index and next greater element index
                span[i] = i - stack[-1]
                
            # Push this element's index to stack
            stack.append(i)
            
        return span