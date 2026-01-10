class Solution:
    def bestNumbers(self, N: int, A: int, B: int, C: int, D: int) -> int:
        MOD = 10**9 + 7
        
        # Precompute factorials and inverse factorials for O(1) nCr
        fact = [1] * (N + 1)
        inv = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = (fact[i - 1] * i) % MOD
            
        # Modular exponentiation for inverse (Fermat's Little Theorem)
        inv[N] = pow(fact[N], MOD - 2, MOD)
        for i in range(N - 1, -1, -1):
            inv[i] = (inv[i + 1] * (i + 1)) % MOD
            
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            num = fact[n]
            den = (inv[r] * inv[n - r]) % MOD
            return (num * den) % MOD

        def is_best(s_val, c, d):
            s_str = str(s_val)
            c_str, d_str = str(c), str(d)
            return c_str in s_str or d_str in s_str

        ans = 0
        
        # Optimization: Handle the case where A == B to avoid duplicate counting
        if A == B:
            digit_sum = N * A
            if is_best(digit_sum, C, D):
                return 1
            return 0

        for i in range(N + 1):
            digit_sum = i * A + (N - i) * B
            
            if is_best(digit_sum, C, D):
                ans = (ans + nCr(N, i)) % MOD
                
        return ans