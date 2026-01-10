class Solution:
    def palindromepair(self, N, arr):
        words = {word: i for i, word in enumerate(arr)}
        
        def is_palindrome(s):
            # Efficiently check palindrome using slicing
            return s == s[::-1]
            
        for i, word in enumerate(arr):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                # Check if reverse(suffix) + word is a palindrome
                if is_palindrome(prefix):
                    rev_suffix = suffix[::-1]
                    if rev_suffix in words and words[rev_suffix] != i:
                        return 1 # Return integer 1 instead of True
                
                # Check if word + reverse(prefix) is a palindrome
                if j < n and is_palindrome(suffix):
                    rev_prefix = prefix[::-1]
                    if rev_prefix in words and words[rev_prefix] != i:
                        return 1 # Return integer 1 instead of True
                        
        return 0 # Return integer 0 instead of False