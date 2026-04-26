class Solution:
    def commonElements(self, a, b, c):
        i, j, k = 0, 0, 0
        result = []
        
        while i < len(a) and j < len(b) and k < len(c):
            
            # If all elements are equal
            if a[i] == b[j] == c[k]:
                # Avoid duplicates
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                
                i += 1
                j += 1
                k += 1
            
            # Move the pointer with smallest value
            elif a[i] < b[j]:
                i += 1
            elif b[j] < c[k]:
                j += 1
            else:
                k += 1
        
        return result