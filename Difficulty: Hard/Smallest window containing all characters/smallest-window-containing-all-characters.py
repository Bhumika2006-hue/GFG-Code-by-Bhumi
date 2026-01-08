from collections import Counter

class Solution:
    def smallestWindow(self, s, p):
        n, m = len(s), len(p)
        if m > n:
            return ""
            
        # Frequency of characters in p
        p_count = Counter(p)
        # Unique characters in p that need to be matched
        required = len(p_count)
        
        # Sliding window variables
        window_count = {}
        formed = 0  # Number of unique characters matched with required frequency
        
        left = 0
        min_len = float('inf')
        start_idx = 0
        
        for right in range(n):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If current character's frequency matches p's frequency
            if char in p_count and window_count[char] == p_count[char]:
                formed += 1
            
            # Try to shrink the window while it's valid
            while formed == required:
                # Update minimum length and start index
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    start_idx = left
                
                # Remove left character from window
                left_char = s[left]
                window_count[left_char] -= 1
                
                # If removing the character makes the window invalid
                if left_char in p_count and window_count[left_char] < p_count[left_char]:
                    formed -= 1
                
                left += 1
        
        return s[start_idx : start_idx + min_len] if min_len != float('inf') else ""