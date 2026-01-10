class Solution:
    def nextHappy(self, N):
        def is_happy(n):
            # Optimization: Unhappy numbers eventually hit the cycle containing 4
            # We only need to check if it hits 1 (Happy) or 4 (Unhappy)
            while n != 1 and n != 4:
                sum_sq = 0
                while n > 0:
                    digit = n % 10
                    sum_sq += digit * digit
                    n //= 10
                n = sum_sq
            
            return n == 1

        # Start checking from the next number
        candidate = N + 1
        while True:
            if is_happy(candidate):
                return candidate
            candidate += 1