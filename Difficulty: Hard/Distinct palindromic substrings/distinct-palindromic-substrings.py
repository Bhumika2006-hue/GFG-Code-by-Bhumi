class Solution:
    def palindromicSubstr(self, s):
        n = len(s)
        distinct_palindromes = set()
        
        def expand_around_center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                # Add the substring to the set
                distinct_palindromes.add(s[left : right + 1])
                # Expand outwards
                left -= 1
                right += 1
                
        for i in range(n):
            # Odd length palindromes (center is a character)
            expand_around_center(i, i)
            
            # Even length palindromes (center is between two characters)
            expand_around_center(i, i + 1)
            
        # The driver code expects a list
        return list(distinct_palindromes)