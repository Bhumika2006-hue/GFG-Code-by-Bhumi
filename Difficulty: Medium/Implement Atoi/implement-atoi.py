class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Convert digits
        num = 0
        found_digit = False
        
        while i < n and s[i].isdigit():
            found_digit = True
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1
            
            # Step 4: Clamp during conversion
            if sign * num >= 2**31 - 1:
                return 2**31 - 1
            if sign * num <= -2**31:
                return -2**31
        
        # Step 5: If no digits found
        if not found_digit:
            return 0
        
        return sign * num
