class Solution:
    def medianOf2(self, a, b):
        # Ensure 'a' is the smaller array to minimize binary search range
        if len(a) > len(b):
            return self.medianOf2(b, a)
            
        n1, n2 = len(a), len(b)
        low, high = 0, n1
        
        while low <= high:
            # i is the partition index for array a
            # j is the partition index for array b
            i = (low + high) // 2
            j = (n1 + n2 + 1) // 2 - i
            
            # Boundary values
            l1 = a[i-1] if i > 0 else float('-inf')
            r1 = a[i] if i < n1 else float('inf')
            
            l2 = b[j-1] if j > 0 else float('-inf')
            r2 = b[j] if j < n2 else float('inf')
            
            # Check if we found the correct partition
            if l1 <= r2 and l2 <= r1:
                # If total elements are odd
                if (n1 + n2) % 2 != 0:
                    return float(max(l1, l2))
                # If total elements are even
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            
            elif l1 > r2:
                # Too far right in 'a', move left
                high = i - 1
            else:
                # Too far left in 'a', move right
                low = i + 1
                
        return 0.0