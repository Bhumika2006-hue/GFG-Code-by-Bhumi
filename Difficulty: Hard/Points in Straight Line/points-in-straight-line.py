from math import gcd

class Solution:
    def maxPoints(self, X, Y, N):
        if N <= 2:
            return N
        
        overall_max = 0
        
        for i in range(N):
            slopes = {}
            duplicates = 1
            current_max = 0
            
            for j in range(i + 1, N):
                dx = X[j] - X[i]
                dy = Y[j] - Y[i]
                
                # Handle duplicate points
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                
                # Simplify the slope fraction using GCD
                common = gcd(dx, dy)
                dx //= common
                dy //= common
                
                # Ensure signs are consistent (e.g., -1/-2 is same as 1/2)
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0: # Vertical line
                    dy = abs(dy)
                
                slope = (dy, dx)
                slopes[slope] = slopes.get(slope, 0) + 1
                current_max = max(current_max, slopes[slope])
            
            # The maximum points for this anchor is the highest slope count + duplicates
            overall_max = max(overall_max, current_max + duplicates)
            
        return overall_max