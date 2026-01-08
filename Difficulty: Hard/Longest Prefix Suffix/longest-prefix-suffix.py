class Solution:
    def getLPSLength(self, s):
        n = len(s)
        if n == 0:
            return 0
            
        # lps[i] stores the length of the longest proper prefix 
        # of s[0...i] which is also a suffix of s[0...i]
        lps = [0] * n
        
        length = 0  # length of the previous longest prefix suffix
        i = 1
        
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                # If characters don't match, we fall back to the 
                # last known matching prefix length
                if length != 0:
                    length = lps[length - 1]
                else:
                    # No match found, set lps to 0 and move to next char
                    lps[i] = 0
                    i += 1
                    
        # The result for the entire string is the last element in the array
        return lps[n-1]