class Solution:
    def toughProblem(self, N, S, X):
        # 1. Basic Parity and Magnitude check
        if S < X or (S - X) % 2 != 0:
            return "No"
        
        # 2. Case for N = 1
        if N == 1:
            return "Yes" if S == X else "No"
        
        # 3. Case for N = 2
        # For N=2, we must check the bitwise AND condition
        if N == 2:
            and_val = (S - X) // 2
            # Condition: (a AND b) and (a XOR b) cannot share set bits
            if (and_val & X) == 0:
                return "Yes"
            else:
                return "No"
        
        # 4. Case for N >= 3
        # If parity and magnitude are correct, N >= 3 is always "Yes"
        return "Yes"