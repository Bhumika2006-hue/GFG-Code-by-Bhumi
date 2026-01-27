class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])
        
        def dfs(i, j, k):
            # All characters matched
            if k == len(word):
                return True
            
            # Out of bounds or mismatch
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != word[k]:
                return False
            
            # Mark visited
            temp = mat[i][j]
            mat[i][j] = '#'
            
            # Explore 4 directions
            found = (dfs(i+1, j, k+1) or
                     dfs(i-1, j, k+1) or
                     dfs(i, j+1, k+1) or
                     dfs(i, j-1, k+1))
            
            # Backtrack
            mat[i][j] = temp
            return found
        
        # Try starting from every cell
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
