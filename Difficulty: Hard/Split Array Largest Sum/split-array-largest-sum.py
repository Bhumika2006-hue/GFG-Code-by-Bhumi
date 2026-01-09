class Solution:
    def splitArray(self, arr, k):
        # Function to check if a max_sum 'mid' is feasible
        def isPossible(mid):
            count = 1
            current_sum = 0
            for x in arr:
                if current_sum + x > mid:
                    # Start a new subarray
                    count += 1
                    current_sum = x
                    if count > k:
                        return False
                else:
                    current_sum += x
            return True

        # Binary search range
        low = max(arr)
        high = sum(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if isPossible(mid):
                ans = mid      # Try to find a smaller maximum sum
                high = mid - 1
            else:
                low = mid + 1  # Need a larger maximum sum to fit into k subarrays
                
        return ans