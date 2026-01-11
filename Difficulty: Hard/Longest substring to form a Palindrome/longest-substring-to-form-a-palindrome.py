class Solution:
    def longestSubstring(self, S):
        # Dictionary to store the first occurrence of each bitmask
        # Initialize with mask 0 at index -1
        first_occurrence = {0: -1}
        
        current_mask = 0
        max_length = 0
        
        for i, char in enumerate(S):
            # Update the mask for the current character
            # ord(char) - ord('a') gives index 0-25
            bit_pos = ord(char) - ord('a')
            current_mask ^= (1 << bit_pos)
            
            # Case 1: All characters in substring have even frequency
            # If current_mask was seen before, the substring between 
            # the two occurrences has all even frequencies.
            if current_mask in first_occurrence:
                max_length = max(max_length, i - first_occurrence[current_mask])
            else:
                # Store only the first time we see this mask to maximize length
                first_occurrence[current_mask] = i
                
            # Case 2: Exactly one character has an odd frequency
            # Check if current_mask XOR (1 << j) was seen before
            for j in range(26):
                target_mask = current_mask ^ (1 << j)
                if target_mask in first_occurrence:
                    max_length = max(max_length, i - first_occurrence[target_mask])
        
        return max_length