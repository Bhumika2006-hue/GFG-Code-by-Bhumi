class Solution:
    def maxSum(self, s):
        n = len(s)
        # Step 1: Manacher's Algorithm for odd lengths
        # d[i] is the radius (e.g., "aba" center 'b' has d=1)
        d = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r - i)
            while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d[i] = k - 1
            if i + d[i] > r:
                l = i - d[i]
                r = i + d[i]

        # Step 2: Calculate max palindrome length ending at each index
        # left[i] = max length of odd palindrome ending exactly at i or before
        left = [1] * n
        for i in range(n):
            # A palindrome centered at i with radius d[i] ends at i + d[i]
            # its length is 2*d[i] + 1
            left[i + d[i]] = max(left[i + d[i]], 2 * d[i] + 1)
        
        # Propagate: If a palindrome of length L ends at i, 
        # a palindrome of length L-2 also ends at i-1
        for i in range(n - 1, 0, -1):
            left[i-1] = max(left[i-1], left[i] - 2)
        # Ensure left[i] is non-decreasing (max length ending at or before i)
        for i in range(1, n):
            left[i] = max(left[i], left[i-1])

        # Step 3: Calculate max palindrome length starting at each index
        right = [1] * n
        for i in range(n):
            # A palindrome centered at i with radius d[i] starts at i - d[i]
            right[i - d[i]] = max(right[i - d[i]], 2 * d[i] + 1)
            
        # Propagate: If a palindrome of length L starts at i, 
        # a palindrome of length L-2 also starts at i+1
        for i in range(n - 1):
            right[i+1] = max(right[i+1], right[i] - 2)
        # Ensure right[i] is max length starting at or after i
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i], right[i+1])

        # Step 4: Find split point to maximize sum
        max_sum = 0
        for i in range(n - 1):
            max_sum = max(max_sum, left[i] + right[i+1])
            
        return max_sum