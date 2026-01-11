from collections import deque
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Helper function to check if a string of parentheses is valid
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0: # More closing than opening at any point
                    return False
            return count == 0

        if not s:
            return [""]

        ans = []
        visited = {s}
        queue = deque([s])
        found = False

        while queue:
            level_size = len(queue)
            
            # Process all nodes at the current depth (current number of removals)
            for _ in range(level_size):
                curr = queue.popleft()
                
                if isValid(curr):
                    ans.append(curr)
                    found = True
                
                # Once we find a valid string, we stop generating new strings
                # because any further removals won't be "minimum".
                if found:
                    continue
                
                # Generate strings for the next level by removing one parenthesis
                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue
                    
                    next_s = curr[:i] + curr[i+1:]
                    if next_s not in visited:
                        visited.add(next_s)
                        queue.append(next_s)
            
            # If we found valid strings at this level, we are done
            if found:
                break
        
        # Return unique valid strings in sorted order
        return sorted(list(set(ans)))