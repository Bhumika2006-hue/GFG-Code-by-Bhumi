class Solution:
    def getLastMoment(self, n, left, right):
        last = 0
        
        for x in left:
            last = max(last, x)
        
        for x in right:
            last = max(last, n - x)
        
        return last
