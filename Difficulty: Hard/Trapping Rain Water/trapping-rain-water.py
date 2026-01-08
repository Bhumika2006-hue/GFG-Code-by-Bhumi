class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n < 3:
            return 0
        
        left = 0
        right = n - 1
        l_max = 0
        r_max = 0
        total_water = 0
        
        while left <= right:
            # Always process the side with the lower potential boundary
            if arr[left] <= arr[right]:
                if arr[left] >= l_max:
                    l_max = arr[left]
                else:
                    total_water += l_max - arr[left]
                left += 1
            else:
                if arr[right] >= r_max:
                    r_max = arr[right]
                else:
                    total_water += r_max - arr[right]
                right -= 1
                
        return total_water