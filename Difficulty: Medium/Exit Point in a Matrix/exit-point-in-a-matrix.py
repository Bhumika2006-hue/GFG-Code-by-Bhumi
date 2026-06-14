class Solution:
    def exitPoint(self, mat):
        n = len(mat)
        m = len(mat[0])

        # Right, Down, Left, Up
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        r, c = 0, 0
        direction = 0  # Initially moving right

        while 0 <= r < n and 0 <= c < m:
            if mat[r][c] == 1:
                direction = (direction + 1) % 4
                mat[r][c] = 0

            nr = r + dr[direction]
            nc = c + dc[direction]

            if not (0 <= nr < n and 0 <= nc < m):
                return [r, c]

            r, c = nr, nc