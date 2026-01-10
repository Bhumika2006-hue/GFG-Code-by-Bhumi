class Solution:
    def findExpr(self, s, target):
        res = []
        n = len(s)

        def backtrack(idx, path, current_val, last_val):
            # Base Case: Reached the end of the string
            if idx == n:
                if current_val == target:
                    res.append(path)
                return

            for j in range(idx, n):
                # Handle Leading Zeros: "05" is invalid, but "0" is fine
                if j > idx and s[idx] == '0':
                    break
                
                # Extract the current substring as a number
                sub_str = s[idx : j + 1]
                val = int(sub_str)

                if idx == 0:
                    # First number in the expression (no operator before it)
                    backtrack(j + 1, sub_str, val, val)
                else:
                    # Case 1: Addition
                    backtrack(j + 1, path + "+" + sub_str, current_val + val, val)
                    
                    # Case 2: Subtraction
                    backtrack(j + 1, path + "-" + sub_str, current_val - val, -val)
                    
                    # Case 3: Multiplication (Undo previous last_val and multiply)
                    # Expression logic: current_val - last_val + (last_val * val)
                    backtrack(j + 1, path + "*" + sub_str, 
                              (current_val - last_val) + (last_val * val), 
                              last_val * val)

        backtrack(0, "", 0, 0)
        return res
        
        