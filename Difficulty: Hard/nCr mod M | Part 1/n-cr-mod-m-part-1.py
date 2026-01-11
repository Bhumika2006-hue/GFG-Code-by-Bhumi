class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1
        if r > n // 2:
            r = n - r
            
        p = 1000003
        
        def nCr_small(n, r, p):
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            if r > n // 2:
                r = n - r
                
            num = 1
            den = 1
            for i in range(r):
                num = (num * (n - i)) % p
                den = (den * (i + 1)) % p
            
            # Using Python's optimized modular inverse: pow(den, p-2, p)
            return (num * pow(den, p - 2, p)) % p

        # Lucas Theorem application
        res = 1
        while n > 0 and res != 0:
            ni = n % p
            ri = r % p
            if ri > ni:
                return 0
            res = (res * nCr_small(ni, ri, p)) % p
            n //= p
            r //= p
            
        return res