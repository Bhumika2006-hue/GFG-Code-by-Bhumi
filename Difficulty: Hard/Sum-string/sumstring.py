class Solution:
    def isSumString(self, s):
        n = len(s)

        def check(s1, s2, remaining):
            if not remaining:
                return True
            
            # Calculate sum of two strings
            # Python handles large integers automatically
            sum_val = str(int(s1) + int(s2))
            
            # If the remaining string starts with our calculated sum
            if remaining.startswith(sum_val):
                # Recursively check the rest of the string
                return check(s2, sum_val, remaining[len(sum_val):])
            
            return False

        # Try all possible splits for the first two numbers
        # i is the end of the first number, j is the end of the second
        for i in range(1, n):
            for j in range(i + 1, n):
                s1 = s[0:i]
                s2 = s[i:j]
                
                # Basic leading zero check (except for "0" itself)
                if (s1.startswith('0') and len(s1) > 1) or \
                   (s2.startswith('0') and len(s2) > 1):
                    continue
                
                # Check if this pair can form a valid sum-string
                if check(s1, s2, s[j:]):
                    return True
                    
        return False