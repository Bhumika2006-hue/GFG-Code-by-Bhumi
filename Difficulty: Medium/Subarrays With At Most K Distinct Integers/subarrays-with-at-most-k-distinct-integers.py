class Solution:
    def countAtMostK(self, arr, k):
        # If k is 0, no subarray can have at most 0 distinct elements 
        # (unless we count empty subarrays, which is usually not the case)
        if k <= 0:
            return 0
            
        n = len(arr)
        left = 0
        total_count = 0
        freq_map = {}
        
        for right in range(n):
            # Add the current element to the frequency map
            char = arr[right]
            freq_map[char] = freq_map.get(char, 0) + 1
            
            # Shrink the window from the left if distinct elements > k
            while len(freq_map) > k:
                left_char = arr[left]
                freq_map[left_char] -= 1
                
                # If frequency becomes 0, remove it from the map to reduce size
                if freq_map[left_char] == 0:
                    del freq_map[left_char]
                
                left += 1
            
            # The number of subarrays ending at 'right' with at most k distinct 
            # elements is equal to the current window size
            total_count += (right - left + 1)
            
        return total_count
        