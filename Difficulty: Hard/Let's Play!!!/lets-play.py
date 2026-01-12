class Solution:
    def isSuperSimilar(self, n, m, mat, x):
        # We only care about x % m because rotating by the 
        # length of the row results in the same row.
        shift = x % m
        
        # If shift is 0, no change occurs, always similar.
        if shift == 0:
            return 1
            
        for i in range(n):
            for j in range(m):
                if i % 2 == 0:
                    # Even index row: Left Rotation
                    # Compare current element with the element 'shift' places ahead
                    if mat[i][j] != mat[i][(j + shift) % m]:
                        return 0
                else:
                    # Odd index row: Right Rotation
                    # Compare current element with the element 'shift' places behind
                    # Python handles negative indices in modulo correctly: (j - shift) % m
                    if mat[i][j] != mat[i][(j - shift) % m]:
                        return 0
                        
        return 1