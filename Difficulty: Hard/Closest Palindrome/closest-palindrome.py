class Solution:
    def closestPalindrome(self, num):
        s = str(num)
        n = len(s)
        
        # Candidate set to store potential palindromes
        candidates = set()
        
        # Case 1 & 2: Boundary cases (99...9 and 10...01)
        candidates.add(10**(n - 1) - 1) # e.g., 1000 -> 999
        candidates.add(10**n + 1)       # e.g., 999 -> 1001
        
        # Extract the prefix
        # If n=5, prefix is 3 digits. If n=4, prefix is 2 digits.
        prefix = int(s[:(n + 1) // 2])
        
        # Case 3, 4, 5: prefix, prefix+1, prefix-1 mirrored
        for i in [-1, 0, 1]:
            p = str(prefix + i)
            # Create palindrome based on even or odd length of original string
            if n % 2 == 0:
                res = p + p[::-1]
            else:
                res = p + p[:-1][::-1]
            candidates.add(int(res))
        
        # We don't want the original number if the problem implies 'closest different',
        # but the problem states 'closest palindrome', so if num is palindrome, it's the answer.
        # However, many platforms expect a different palindrome if available.
        # Let's check the distance for all.
        
        closest_val = -1
        min_diff = float('inf')
        num_int = int(num)
        
        # Sort candidates to handle the "take smaller one" rule easily
        for cand in sorted(list(candidates)):
            if cand == num_int:
                return num_int
            
            diff = abs(cand - num_int)
            if diff < min_diff:
                min_diff = diff
                closest_val = cand
                
        return closest_val