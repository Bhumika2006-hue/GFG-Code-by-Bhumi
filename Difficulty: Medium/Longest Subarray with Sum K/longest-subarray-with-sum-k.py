class Solution:
    def longestSubarray(self, arr, k):
        # Dictionary to store (prefix_sum: first_occurrence_index)
        sum_map = {}
        prefix_sum = 0
        max_length = 0
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            # Case 1: Prefix sum itself is equal to k
            if prefix_sum == k:
                max_length = i + 1
            
            # Case 2: Check if (prefix_sum - k) exists in map
            # If it exists, the subarray between that index and i sums to k
            if (prefix_sum - k) in sum_map:
                max_length = max(max_length, i - sum_map[prefix_sum - k])
            
            # Case 3: Only add prefix_sum to map if it's NOT already there
            # This ensures we keep the leftmost index for the longest subarray
            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i
                
        return max_length