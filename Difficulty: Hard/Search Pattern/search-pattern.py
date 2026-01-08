class Solution:
    def search(self, pat, txt):
        n = len(txt)
        m = len(pat)
        
        # 1. Precompute LPS array
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        # 2. Pattern Matching
        result = []
        i = 0 # index for txt
        j = 0 # index for pat
        
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
            
            if j == m:
                # Pattern found! Add starting index
                result.append(i - j)
                # Continue searching for next occurrence
                j = lps[j - 1]
            elif i < n and txt[i] != pat[j]:
                # Mismatch after j matches
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
                    
        return result