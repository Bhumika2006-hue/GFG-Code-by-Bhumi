class Solution:
    def evenlyDivides(self, n):
        count = 0
        temp = n

        while temp > 0:
            digit = temp % 10
            temp //= 10

            if digit != 0 and n % digit == 0:
                count += 1

        return count
