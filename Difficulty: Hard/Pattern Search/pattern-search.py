class Solution:
    def search(self, p, s):
        M = len(p)
        N = len(s)
        
        if M == 0: return True
        if M > N: return False

        # Step 1: Precompute the LPS array
        lps = [0] * M
        length = 0  # length of the previous longest prefix suffix
        i = 1
        
        while i < M:
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # Step 2: Perform the search
        i = 0  # index for s
        j = 0  # index for p
        while i < N:
            if p[j] == s[i]:
                i += 1
                j += 1
            
            if j == M:
                return True # Pattern found
            
            # Mismatch after j matches
            elif i < N and p[j] != s[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
                    
        return False