class Solution:
    def findPosition(self, n):
        # Edge case: no set bit
        if n == 0:
            return -1
        
        # Check if more than one set bit exists
        if (n & (n - 1)) != 0:
            return -1
        
        # Find position of the only set bit
        pos = 1
        while n > 1:
            n = n >> 1
            pos += 1
        
        return pos