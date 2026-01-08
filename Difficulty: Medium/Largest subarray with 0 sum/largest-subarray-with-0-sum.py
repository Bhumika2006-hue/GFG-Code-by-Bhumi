class Solution:
    def maxLength(self, arr):
        # hash_map stores the first occurrence of each prefix sum: {prefix_sum: index}
        hash_map = {}
        max_length = 0
        curr_sum = 0
        
        for i in range(len(arr)):
            curr_sum += arr[i]
            
            # Case 1: The prefix sum itself is zero
            if curr_sum == 0:
                max_length = i + 1
            
            # Case 2: The prefix sum has been seen before
            if curr_sum in hash_map:
                # Calculate the distance from the first occurrence to now
                length = i - hash_map[curr_sum]
                if length > max_length:
                    max_length = length
            else:
                # Case 3: First time seeing this prefix sum, store its index
                hash_map[curr_sum] = i
                
        return max_length