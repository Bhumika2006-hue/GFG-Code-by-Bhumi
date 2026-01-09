class Solution:
    def permutation(self, s):
        n = len(s)
        chars = list(s)
        # We will work with indices to ensure we generate ALL N! permutations
        indices = list(range(n))
        result = []
        
        def backtrack(start):
            if start == n:
                # Map the current index permutation back to the actual characters
                res_str = "".join(chars[i] for i in indices)
                result.append(res_str)
                return
            
            for i in range(start, n):
                # Swap current index with the loop index
                indices[start], indices[i] = indices[i], indices[start]
                
                # Recurse for the next position
                backtrack(start + 1)
                
                # Backtrack: swap back to restore original state
                indices[start], indices[i] = indices[i], indices[start]
        
        # 1. Generate all N! permutations
        backtrack(0)
        
        # 2. Sort the final list to meet the "lexicographically increasing" requirement
        result.sort()
        
        return result