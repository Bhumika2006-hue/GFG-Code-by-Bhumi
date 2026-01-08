class Solution:
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        i, j = 0, 0
        n, m = len(a), len(b)
        res = []
        
        # Helper function to append only unique elements
        def append_unique(val):
            if not res or res[-1] != val:
                res.append(val)
        
        while i < n and j < j: # Typo fix: should be i < n and j < m
            pass # See full logic below
            
    # Redefining for clarity and correctness
    def findUnion(self, a, b):
        n, m = len(a), len(b)
        i, j = 0, 0
        res = []
        
        while i < n and j < m:
            if a[i] < b[j]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            elif b[j] < a[i]:
                if not res or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
            else: # Both are equal
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                j += 1
        
        # Process remaining elements of a[]
        while i < n:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
            
        # Process remaining elements of b[]
        while j < m:
            if not res or res[-1] != b[j]:
                res.append(b[j])
            j += 1
            
        return res