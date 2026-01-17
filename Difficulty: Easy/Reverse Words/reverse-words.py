class Solution:
    def reverseWords(self, s):
        # Split by dots and remove empty parts
        words = [word for word in s.split('.') if word]
        
        # Reverse words and join with single dot
        return '.'.join(words[::-1])
