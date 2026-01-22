class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)
        
        def get_total_contribution(is_max):
            # Using a monotonic stack to find bounds
            total = 0
            # stack stores indices
            stack = []
            
            # We add a sentinel value to the end to flush the stack at the end
            for i in range(n + 1):
                while stack and (i == n or (arr[stack[-1]] < arr[i] if is_max else arr[stack[-1]] > arr[i])):
                    mid = stack.pop()
                    left_bound = stack[-1] if stack else -1
                    right_bound = i
                    
                    # Count of subarrays where arr[mid] is the extremum
                    count = (mid - left_bound) * (right_bound - mid)
                    total += count * arr[mid]
                stack.append(i)
            return total

        return get_total_contribution(True) - get_total_contribution(False)