class Solution:
    def minWindow(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        i, j = 0, 0
        min_len = float('inf')
        start_index = -1
        
        while i < n1:
            # Forward Pass: find s2 as subsequence in s1
            if s1[i] == s2[j]:
                j += 1
                # If we matched all characters of s2
                if j == n2:
                    end = i
                    j -= 1
                    # Backward Pass: shrink the window from the right to the left
                    while j >= 0:
                        if s1[i] == s2[j]:
                            j -= 1
                        i -= 1
                    
                    # Window is from i+1 to end
                    i += 1
                    current_len = end - i + 1
                    if current_len < min_len:
                        min_len = current_len
                        start_index = i
                    
                    # Reset j to start looking for the next window
                    j = 0
            i += 1
            
        if start_index == -1:
            return ""
        return s1[start_index : start_index + min_len]