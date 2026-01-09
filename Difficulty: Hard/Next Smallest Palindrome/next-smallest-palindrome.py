class Solution:
    def generateNextPalindrome(self, num, n):
        # Case 1: All 9s
        if all(d == 9 for d in num):
            res = [0] * (n + 1)
            res[0] = res[-1] = 1
            return res

        mid = n // 2
        i = mid - 1
        j = mid if n % 2 == 0 else mid + 1
        
        # Skip digits that are already equal in mirrored positions
        while i >= 0 and num[i] == num[j]:
            i -= 1
            j += 1
            
        left_smaller = False
        # If we reached the end or the left digit is smaller than right
        if i < 0 or num[i] < num[j]:
            left_smaller = True
            
        # Copy left half to right half
        while i >= 0:
            num[j] = num[i]
            i -= 1
            j += 1
            
        # Case 3: If mirroring made it smaller/equal, increment from the middle
        if left_smaller:
            carry = 1
            i = mid - 1
            
            if n % 2 == 1: # Odd length
                num[mid] += carry
                carry = num[mid] // 10
                num[mid] %= 10
                j = mid + 1
            else: # Even length
                j = mid
                
            # Propagate carry to the left and mirror to the right
            while i >= 0:
                num[i] += carry
                carry = num[i] // 10
                num[i] %= 10
                num[j] = num[i]
                i -= 1
                j += 1
                
        return num