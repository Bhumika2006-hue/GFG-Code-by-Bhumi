class Solution:
    def findOccurrence(self, mat, target):
        R = len(mat)
        C = len(mat[0])
        target_len = len(target)
        
        def backtrack(r, c, index):
            # Boundary checks and character match check
            if r < 0 or r >= R or c < 0 or c >= C or mat[r][c] != target[index]:
                return 0
            
            # Base Case: If this was the last character of the target
            if index == target_len - 1:
                return 1
            
            # Found a match, mark visited and explore neighbors
            temp = mat[r][c]
            mat[r][c] = '#'
            
            count = 0
            # Explore Up, Down, Left, Right
            count += backtrack(r + 1, c, index + 1)
            count += backtrack(r - 1, c, index + 1)
            count += backtrack(r, c + 1, index + 1)
            count += backtrack(r, c - 1, index + 1)
            
            # Backtrack: Restore the cell
            mat[r][c] = temp
            
            return count

        total_occurrences = 0
        for i in range(R):
            for j in range(C):
                # Start searching if the first character matches
                if mat[i][j] == target[0]:
                    total_occurrences += backtrack(i, j, 0)
        
        return total_occurrences