class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        def is_possible(target_h):
            # days_needed tracks total days used
            days_needed = 0
            # diff array to handle range updates in O(1)
            diff = [0] * (n + 1)
            # current_extra_h is the height added to the current flower
            current_extra_h = 0
            
            for i in range(n):
                # Apply updates from previous windows ending here
                current_extra_h += diff[i]
                
                actual_h = arr[i] + current_extra_h
                
                if actual_h < target_h:
                    # How many more waterings are needed for this flower?
                    needed = target_h - actual_h
                    days_needed += needed
                    
                    if days_needed > k:
                        return False
                    
                    # Apply range update: current flower to i + w - 1
                    current_extra_h += needed
                    if i + w < n:
                        diff[i + w] -= needed
            
            return days_needed <= k

        # Binary Search Range
        low = min(arr)
        high = min(arr) + k
        ans = low

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans