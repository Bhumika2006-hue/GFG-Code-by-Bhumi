class Solution: 
    def chocolatePickup(self, mat): 
        n = len(mat)
        # memo stores max chocolates for (step, r1, r2)
        # Initialize with -infinity
        memo = {}

        def solve(k, r1, r2):
            c1 = k - r1
            c2 = k - r2
            
            # Out of bounds or blocked cell check
            if (r1 >= n or r2 >= n or c1 >= n or c2 >= n or 
                mat[r1][c1] == -1 or mat[r2][c2] == -1):
                return float('-inf')
            
            # Destination reached
            if k == 2 * n - 2:
                return mat[r1][c1]
            
            state = (k, r1, r2)
            if state in memo:
                return memo[state]
            
            # Current chocolates collected
            res = mat[r1][c1]
            if r1 != r2:
                res += mat[r2][c2]
            
            # Four possible combinations of moves for the two paths:
            # (Down, Down), (Down, Right), (Right, Down), (Right, Right)
            nxt = max(
                solve(k + 1, r1 + 1, r2 + 1),
                solve(k + 1, r1 + 1, r2),
                solve(k + 1, r1, r2 + 1),
                solve(k + 1, r1, r2)
            )
            
            memo[state] = res + nxt
            return memo[state]

        result = solve(0, 0, 0)
        return max(0, result)