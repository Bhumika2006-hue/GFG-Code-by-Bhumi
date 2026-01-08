class Solution:
    def maxLength(self, s):
        # Stack to store indices of characters
        # Initialize with -1 as a base for length calculation
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push index of opening parenthesis
                stack.append(i)
            else:
                # We found a closing parenthesis, pop the last matching opening or base
                stack.pop()
                
                if not stack:
                    # If stack is empty, push current index as new base
                    stack.append(i)
                else:
                    # Current length = current index - index of the previous base
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len