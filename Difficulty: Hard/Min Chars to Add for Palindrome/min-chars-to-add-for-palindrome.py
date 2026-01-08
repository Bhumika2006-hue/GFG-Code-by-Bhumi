class Solution:
    def minChar(self, s):
        n = len(s)
        # Create the combined string: original + separator + reversed
        rev_s = s[::-1]
        combined = s + "$" + rev_s
        
        # Build the LPS array for the combined string
        m = len(combined)
        lps = [0] * m
        
        # Standard KMP LPS calculation
        length = 0
        i = 1
        while i < m:
            if combined[i] == combined[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        # Longest palindromic prefix length is lps[-1]
        longest_palindromic_prefix_len = lps[-1]
        
        # Characters to add = Total length - longest palindromic prefix length
        return n - longest_palindromic_prefix_len