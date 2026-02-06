class Solution:
    def smallestDiff(self, a, b, c):
        a.sort()
        b.sort()
        c.sort()
        
        i = j = k = 0
        best_diff = float('inf')
        best_sum = float('inf')
        ans = []
        
        while i < len(a) and j < len(b) and k < len(c):
            x, y, z = a[i], b[j], c[k]
            mn = min(x, y, z)
            mx = max(x, y, z)
            
            diff = mx - mn
            s = x + y + z
            
            if diff < best_diff or (diff == best_diff and s < best_sum):
                best_diff = diff
                best_sum = s
                ans = sorted([x, y, z], reverse=True)
            
            # move pointer pointing to minimum
            if mn == x:
                i += 1
            elif mn == y:
                j += 1
            else:
                k += 1
        
        return ans
