class Solution:
    def increasingNumbers(self, n):
        if n > 9:
            return []
        
        result = []
        
        def backtrack(start, current_digits):
            if len(current_digits) == n:
                # Form the number from digits
                num = 0
                for d in current_digits:
                    num = num * 10 + d
                result.append(num)
                return
            
            # Digits remaining must be enough to fill remaining slots
            remaining_needed = n - len(current_digits)
            for digit in range(start, 10):
                # Prune: not enough digits left from 'digit' to 9
                if 10 - digit < remaining_needed:
                    break
                current_digits.append(digit)
                backtrack(digit + 1, current_digits)
                current_digits.pop()
        
        if n == 1:
            return list(range(10))  # 0 through 9
        else:
            # Start from 1 to avoid leading zero
            backtrack(1, [])
            return result