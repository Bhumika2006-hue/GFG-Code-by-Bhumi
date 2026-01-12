import math
from typing import List

class Solution:
    def findOptimumCost(self, line : List[int], n : int, points : List[List[int]]) -> float:
        a, b, c = line
        
        # Function to calculate total distance from a point (x, y) on the line
        def get_total_dist(x):
            # Calculate y from ax + by + c = 0 => y = -(ax + c) / b
            y = -1 * (a * x + c) / b
            res = 0
            for px, py in points:
                res += math.sqrt((x - px)**2 + (y - py)**2)
            return res

        # Ternary search range for x
        low = -1000.0
        high = 1000.0
        
        # Run for a fixed number of iterations to ensure precision (around 70-100 is enough)
        for _ in range(100):
            m1 = low + (high - low) / 3
            m2 = high - (high - low) / 3
            
            dist1 = get_total_dist(m1)
            dist2 = get_total_dist(m2)
            
            if dist1 < dist2:
                high = m2
            else:
                low = m1
                
        # Return the minimum distance found
        return round(get_total_dist(low), 2)