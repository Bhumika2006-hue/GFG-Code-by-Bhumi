class Solution:
    def cntCoprime(self, arr):
        n = len(arr)
        if n < 2: return 0
        
        max_val = max(arr)
        
        # Step 1: Count frequency of each number
        freq = [0] * (max_val + 1)
        for x in arr:
            freq[x] += 1
            
        # Step 2: Precompute Mobius function using a sieve
        mu = [0] * (max_val + 1)
        mu[1] = 1
        primes = []
        is_prime = [True] * (max_val + 1)
        
        for i in range(2, max_val + 1):
            if is_prime[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if i * p > max_val:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    mu[i * p] = 0
                    break
                else:
                    mu[i * p] = -mu[i]

        # Step 3: Count multiples for each d
        ans = 0
        for d in range(1, max_val + 1):
            if mu[d] == 0:
                continue
            
            # Count how many elements in arr are multiples of d
            count_d = 0
            for multiple in range(d, max_val + 1, d):
                count_d += freq[multiple]
            
            # Add/Subtract the number of pairs based on Mobius value
            pairs = (count_d * (count_d - 1)) // 2
            ans += mu[d] * pairs
            
        return ans