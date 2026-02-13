class Solution:
    def getCount(self, n, d):
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        
        start = d + 90
        count = 0
        
        if start <= n:
            count += n - start + 1
        
        for x in range(max(1, d), min(n, start - 1) + 1):
            if x - digit_sum(x) >= d:
                count += 1
        
        return count
