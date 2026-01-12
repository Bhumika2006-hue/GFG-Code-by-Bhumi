class Solution:
    def maxFrequency(self, S):
        n = len(S)
        if n == 0:
            return 0
            
        # Step 1: Compute Z-array
        # z[i] is the length of the longest common prefix 
        # between S and S[i:]
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and S[z[i]] == S[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        
        # Step 2: Identify all prefix-suffix lengths
        # A length 'L' is a prefix-suffix if S[0:L] == S[n-L:n]
        # This happens if i + z[i] == n
        borders = []
        for i in range(1, n):
            if i + z[i] == n:
                borders.append(z[i])
        # The full string is always its own prefix and suffix
        borders.append(n)
        
        # Step 3: Count frequencies of all prefix lengths
        # Any z[i] = k means the prefix of length k appears starting at i.
        # This also means prefixes of length 1, 2, ..., k-1 also appear there.
        freq = [0] * (n + 1)
        for i in range(n):
            if i == 0:
                freq[n] += 1
            else:
                freq[z[i]] += 1
        
        # Accumulate frequencies backwards: 
        # a prefix of length 5 also contributes to the count of length 4, 3, etc.
        for i in range(n - 1, 0, -1):
            freq[i] += freq[i + 1]
            
        # Step 4: Find the max frequency among valid borders
        max_f = 0
        for b in borders:
            max_f = max(max_f, freq[b])
            
        return max_f