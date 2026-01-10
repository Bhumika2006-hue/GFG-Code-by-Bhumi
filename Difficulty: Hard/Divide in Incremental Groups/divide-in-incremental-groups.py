class Solution:
    def countWaystoDivide(self, N, K):
        # memo dictionary to store computed states
        memo = {}

        def solve(remaining_sum, remaining_k, min_val):
            # Base Case: If we have used all K elements
            if remaining_k == 0:
                # If the sum is also 0, we found a valid way
                return 1 if remaining_sum == 0 else 0
            
            # If we need more elements but sum is exhausted
            if remaining_sum <= 0:
                return 0
            
            # State identifier
            state = (remaining_sum, remaining_k, min_val)
            if state in memo:
                return memo[state]
            
            ways = 0
            # To ensure non-decreasing order, the next value must be >= min_val
            # To ensure we can finish the sum, next value must be <= remaining_sum // remaining_k
            for val in range(min_val, (remaining_sum // remaining_k) + 1):
                ways += solve(remaining_sum - val, remaining_k - 1, val)
            
            memo[state] = ways
            return ways

        # We start with sum N, needing K elements, and the first element must be at least 1
        return solve(N, K, 1)