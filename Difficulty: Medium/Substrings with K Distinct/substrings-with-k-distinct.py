class Solution:
    def countSubstr (self, s, k):
        return self.atMostK(s, k) - self.atMostK(s, k - 1)

    def atMostK(self, s, k):
        if k < 0: return 0
        
        count = 0
        left = 0
        freq = {}
        
        for right in range(len(s)):
            # Add current character to window
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            # If distinct characters exceed k, shrink window from left
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            
            # All substrings ending at 'right' from 'left' to 'right' 
            # have at most k distinct characters
            count += (right - left + 1)
            
        return count