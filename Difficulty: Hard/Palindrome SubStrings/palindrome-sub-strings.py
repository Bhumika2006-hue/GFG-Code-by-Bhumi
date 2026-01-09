class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0
        
        def expand(left, right):
            nonlocal count
            # Expand as long as pointers are in bounds and characters match
            while left >= 0 and right < n and s[left] == s[right]:
                # The problem asks for length >= 2
                if right - left + 1 >= 2:
                    count += 1
                left -= 1
                right += 1

        for i in range(n):
            # Case 1: Odd length palindromes (center is s[i])
            expand(i, i)
            
            # Case 2: Even length palindromes (center is between s[i] and s[i+1])
            expand(i, i + 1)
            
        return count