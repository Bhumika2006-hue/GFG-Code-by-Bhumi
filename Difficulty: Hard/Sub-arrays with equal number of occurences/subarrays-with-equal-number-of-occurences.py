class Solution:
    def sameOccurrence(self, arr, x, y):
        # Edge case: If x and y are the same, every subarray is valid
        if x == y:
            n = len(arr)
            return (n * (n + 1)) // 2
            
        count_map = {0: 1}
        current_diff = 0
        total_subarrays = 0
        
        for val in arr:
            if val == x:
                current_diff += 1
            elif val == y:
                current_diff -= 1
            
            # Standard prefix sum counting logic
            if current_diff in count_map:
                total_subarrays += count_map[current_diff]
                count_map[current_diff] += 1
            else:
                count_map[current_diff] = 1
                
        return total_subarrays