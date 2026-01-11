class Solution:
    def getLongestPrefix(self, s):
        n = len(s)
        if n < 2:
            return -1
        
        # Step 1: Compute LPS array (Longest Prefix Suffix)
        lps = [0] * n
        j = 0 # length of previous longest prefix suffix
        
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j-1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j
        
        # Step 2: Find the smallest non-zero border
        # The longest border is lps[n-1]. 
        # Shorter borders can be found by traversing lps.
        curr_border = lps[n-1]
        
        if curr_border == 0:
            return -1
        
        smallest_border = curr_border
        while curr_border > 0:
            smallest_border = curr_border
            curr_border = lps[curr_border - 1]
            
        # The longest periodic prefix length L corresponds to 
        # the smallest period, where Period = Total_Length - Smallest_Border
        # Result = n - smallest_border
        return n - smallest_border