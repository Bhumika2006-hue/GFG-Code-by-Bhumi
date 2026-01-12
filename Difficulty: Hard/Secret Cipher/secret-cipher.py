class Solution:
    def compress(self, s):
        n = len(s)
        # Step 1: Compute LPS array for the entire string S
        lps = [0] * n
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
            lps[i] = j
            
        res = []
        i = n - 1
        
        # Step 2: Traverse backwards to find compression points
        while i >= 0:
            # Check if current length (i+1) is even
            curr_len = i + 1
            if curr_len % 2 == 0:
                half = curr_len // 2
                
                # Use a modified LPS check to see if S[0...half-1] == S[half...i]
                # We need to find if there's a prefix-suffix of length exactly half
                # We trace back the LPS to see if 'half' is a valid prefix-suffix length
                temp_lps = lps[i]
                while temp_lps > half:
                    temp_lps = lps[temp_lps - 1]
                
                if temp_lps == half:
                    res.append('*')
                    i = half - 1  # Skip the second half as it's now represented by '*'
                    continue
            
            # If not compressible, add the character itself
            res.append(s[i])
            i -= 1
            
        # Step 3: Reverse the result since we processed it backwards
        return "".join(res[::-1])