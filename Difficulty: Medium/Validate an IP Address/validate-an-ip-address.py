class Solution:
    def isValid(self, s):
        parts = s.split('.')

        # Must have exactly 4 parts
        if len(parts) != 4:
            return False

        for part in parts:
            # Empty part or non-digit
            if not part or not part.isdigit():
                return False

            # Leading zero check
            if len(part) > 1 and part[0] == '0':
                return False

            num = int(part)
            if num < 0 or num > 255:
                return False

        return True
