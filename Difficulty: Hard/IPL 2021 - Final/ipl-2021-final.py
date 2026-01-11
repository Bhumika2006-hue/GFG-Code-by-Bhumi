class Solution:
    def findMaxLen(ob, S):
        # Stack to store indices of parentheses
        # Initialized with -1 to handle the base case
        stack = [-1]
        max_len = 0
        
        for i in range(len(S)):
            if S[i] == '(':
                # Push the index of '('
                stack.append(i)
            else:
                # We found a ')', pop the matching '(' or the base
                stack.pop()
                
                if not stack:
                    # If empty, this ')' is an anchor for the next potential valid substring
                    stack.append(i)
                else:
                    # Calculate current length: current index - index of the new top
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len