class Solution:
    def maxCircularSum(self, arr):
        n = len(arr)
        
        # Variables for Max Subarray Sum (Kadane's)
        max_total = -float('inf')
        current_max = 0
        
        # Variables for Min Subarray Sum
        min_total = float('inf')
        current_min = 0
        
        total_sum = 0
        
        for x in arr:
            total_sum += x
            
            # Standard Kadane's to find max subarray
            current_max += x
            if current_max > max_total:
                max_total = current_max
            if current_max < 0:
                current_max = 0
                
            # Modified Kadane's to find min subarray
            current_min += x
            if current_min < min_total:
                min_total = current_min
            if current_min > 0:
                current_min = 0
        
        # If all elements are negative, the circular sum (total_sum - min_total) 
        # would result in an empty subarray (0). We must return the max_total.
        if max_total < 0:
            return max_total
            
        # The maximum is either the linear sum or the circular (wrapped) sum
        return max(max_total, total_sum - min_total)