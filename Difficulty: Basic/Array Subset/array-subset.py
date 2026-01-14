class Solution:
    # Function to check if b is a subset of a
    def isSubset(self, a, b):
        from collections import Counter
        
        freq = Counter(a)
        
        for x in b:
            if freq[x] == 0:
                return False
            freq[x] -= 1
        
        return True
