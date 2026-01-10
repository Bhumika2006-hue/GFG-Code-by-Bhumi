from typing import List

class Solution:
    def goodSubsets(self, n: int, arr: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        # Count frequency of each number
        count = [0] * 31
        for x in arr:
            count[x] += 1
            
        # Precompute masks for numbers 2-30
        masks = {}
        for i in range(2, 31):
            temp = i
            mask = 0
            is_valid = True
            for j, p in enumerate(primes):
                if temp % (p * p) == 0:
                    is_valid = False
                    break
                if temp % p == 0:
                    mask |= (1 << j)
            if is_valid:
                masks[i] = mask

        # dp[mask] = number of ways to form a subset with prime factors 'mask'
        dp = [0] * (1 << 10)
        dp[0] = 1 # Empty subset base case
        
        for num in range(2, 31):
            if count[num] == 0 or num not in masks:
                continue
            
            num_mask = masks[num]
            # Iterate backwards through DP to avoid using the same number twice 
            # in the same subset (standard 0/1 Knapsack logic)
            for mask in range((1 << 10) - 1, -1, -1):
                if (mask & num_mask) == 0:
                    dp[mask | num_mask] = (dp[mask | num_mask] + dp[mask] * count[num]) % MOD
        
        # Total good subsets (excluding the empty set)
        ans = sum(dp[1:]) % MOD
        
        # Multiply by 2^count[1] because each '1' can either be in or out of a subset
        if count[1] > 0:
            ans = (ans * pow(2, count[1], MOD)) % MOD
            
        return ans