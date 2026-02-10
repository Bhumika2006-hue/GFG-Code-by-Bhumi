import math

class Solution:
    def kokoEat(self, arr, k):
        low, high = 1, max(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            hours = 0
            
            for pile in arr:
                hours += (pile + mid - 1) // mid  # ceil division
            
            if hours <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
