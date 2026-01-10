class Solution:
    def wordBreak(self, dict, s):
        # Convert list to set for O(1) lookups
        word_set = set(dict)
        # Memoization dictionary to store results of suffixes
        memo = {}

        def solve(s):
            # If suffix already processed, return stored result
            if s in memo:
                return memo[s]
            
            # Base Case: end of string reached
            if not s:
                return [""]
            
            res = []
            # Try every possible prefix of the current string
            for i in range(1, len(s) + 1):
                prefix = s[:i]
                
                if prefix in word_set:
                    # Recursively solve for the remaining suffix
                    suffixes = solve(s[i:])
                    
                    for suffix in suffixes:
                        # Combine prefix and suffix with a space if suffix isn't empty
                        if suffix == "":
                            res.append(prefix)
                        else:
                            res.append(prefix + " " + suffix)
            
            memo[s] = res
            return res

        return solve(s)