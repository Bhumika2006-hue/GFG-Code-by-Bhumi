class Solution:
    def countBits(self, N, A):
        MOD = 10**9 + 7
        total_sum = 0
        
        # Iterate through each bit position from 0 to 30
        for k in range(31):
            count_on = 0
            
            # Count how many numbers have the k-th bit set
            for num in A:
                if (num >> k) & 1:
                    count_on += 1
            
            # Numbers that have the k-th bit as 0
            count_off = N - count_on
            
            # Contribution to the sum:
            # Each pair of (1, 0) and (0, 1) contributes 1 to the sum
            # (count_on * count_off) for (i, j) where A[i] has bit 1 and A[j] has 0
            # (count_off * count_on) for (i, j) where A[i] has bit 0 and A[j] has 1
            bit_contribution = (count_on * count_off * 2) % MOD
            
            total_sum = (total_sum + bit_contribution) % MOD
            
        return total_sum