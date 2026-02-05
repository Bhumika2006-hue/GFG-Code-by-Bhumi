class Solution:
    def getMinMax(self, arr):
        mn = float('inf')
        mx = float('-inf')
        
        for x in arr:
            if x < mn:
                mn = x
            if x > mx:
                mx = x
        
        return [mn, mx]
