
from typing import List

from math import comb

class Solution:
    def findNthNumber(self, n: int, k: int) -> int:
        # Precompute combinations (nCr) to speed up the counting process
        # C[i][j] stores the number of ways to choose j positions out of i
        C = [[0] * 65 for _ in range(65)]
        for i in range(65):
            for j in range(i + 1):
                C[i][j] = comb(i, j)

        def countWithAtMostK(X, k):
            """Returns count of numbers in range [0, X] having at most k set bits."""
            res = 0
            set_bits = 0
            
            # Iterate through bits from most significant to least significant
            for i in range(63, -1, -1):
                if (X >> i) & 1:
                    # If we set this bit to 0 instead of 1, we can pick j bits 
                    # from the remaining i positions
                    remaining_k = k - set_bits
                    if remaining_k >= 0:
                        for j in range(min(i, remaining_k) + 1):
                            res += C[i][j]
                    
                    set_bits += 1
            
            # Check if X itself is a 'loved' number
            if set_bits <= k:
                res += 1
            return res

        # Binary search for the nth number
        low = 0
        high = 10**16 # Answer is guaranteed to fit in 64-bit
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if countWithAtMostK(mid, k) >= n:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

        
